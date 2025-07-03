import random

def check_hit_and_blow(secret, guess):
  """ユーザーの推測値と正解を比較して，ヒットとブローの数を返す．"""
  
  # ヒットとブロー変数の初期化
  hit = 0
  blow = 0
  
  # ヒットのカウント(ヒット＝数字と位置があっている)
  for i in range(len(secret)):
    if secret[i] == guess[i]:
      hit += 1
  
  return hit, blow

# ゲーム開始の説明
print('ゲームを開始します．')
print('私が 1 ~ 9 までの数値を使ってランダムな数を作ります．')
print('あなたは 1 桁から 9 桁の桁数を指定してください．')

#  桁数入力
while True:
    n = int(input('何桁の数字でゲームをしますか？(1 ~ 9):'))
    
    # 1 ~ 9 の入力がされたらループを抜ける
    if 1 <= n <= 9:
        break
    print('1 ~ 9 の範囲で入力してください．')

# 正解の数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
secret_numbers = random.sample(numbers, n)
print(secret_numbers)

# 試行回数を初期化
trial_count = 0

# ゲームループ
while True:
    # ユーザーの入力
    guess_number = input(f'{n}桁の数値を入力してください:')
    
    # 入力を整数のリストに変換
    guess_list =[]
    for char in guess_number:
        guess_list.append(int(char))
    print(guess_list)
    
    # 試行回数をカウントアップ
    trial_count += 1
    print(f'{trial_count}回目の回答です．')
    
    # ユーザーの推測値を正解と比較し，ヒット数とブロー数を返す
    hit, blow = check_hit_and_blow(secret_numbers, guess_list)
    print(f'ヒット: {hit}, ブロー: {blow}')