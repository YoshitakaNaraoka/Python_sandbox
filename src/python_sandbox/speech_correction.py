import speech_recognition as sr
import re

def tamego_to_teineigo(text):
    """タメ口を丁寧語に変換する関数"""
    
    # 変換パターン
    patterns = {
        r'だね$': 'ですね',
        r'こんにちは': 'ごきげんよう',
        r'だ$': 'です',
        r'^よう': 'やあ',
        r'しようぜ$': 'しましょう',
        r'飯': 'ご飯',
        r'いいね': 'いいですね',
    }
    
    # ひらがなの重複削除を行わないワードリスト
    no_remove_hiragana = ['いいですね']
    
    # テキストをスペースで分離する
    sentences = text.split(' ')

    # 変換
    teineigo_sentences = []
    dummy_mapping = []
    for sentence in sentences:
        for pattern, replacement in patterns.items():
            sentence = re.sub(pattern, replacement, sentence)
        
        # 重複削除を行わない文字列はダミー文字列に置き換える
        for no_remove in no_remove_hiragana:
            if no_remove in sentence:
                dummy_text = 'X' * len(no_remove)
                dummy_mapping.append((dummy_text, no_remove))
                sentence = sentence.replace(no_remove, dummy_text)
            
        # ひらがなの重複削除を行う
        sentence = re.sub(r'([ぁ-ん ])\1+', r'\1', sentence)
        
        # ダミー文字列を元に戻す
        for dummy_text, original_text in dummy_mapping:
            sentence = sentence.replace(dummy_text, original_text)

        teineigo_sentences.append(sentence)

    joined_text = ' '.join(teineigo_sentences)
    
    return joined_text
  
r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print('マイクに向かってタメ口で話しかけてください')
    audio = r.listen(source)
    
try:
    recognized_text = r.recognize_google(audio, language='ja')
    print(f'音声認識結果「{recognized_text}」')
    teinei_text = tamego_to_teineigo(recognized_text)
    print(f'丁寧語変換結果「{teinei_text}」')
except sr.UnknownValueError:
    print('認識できませんでした．')
except sr.RequestError as e:
    print('ネットワークエラーが発生しました．')