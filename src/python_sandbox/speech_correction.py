import speech_recognition as sr

def tamego_to_teineigo(text):
    """タメ口を丁寧語に変換する関数"""
    
    # 変換パターン
    patterns = {'だね': 'ですね'}
    
    return text
  
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