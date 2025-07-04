print('1から100までの間で好きな数字を1つ思い浮かべてください．')
print('あなたの考えている数字を7回以内に当ててみましょう．')

# low: 最小の数値，high: 最大の数値
low = 1
high = 100
print(low, high)

for i in range(7):
    # low と high が同じならループを抜ける
    if low == high:
        break
    
    # コンピューターの推測値を確認
    guess = (low + high) // 2
    print('あなたの数字は', guess, 'より大きいですか？(yes/no)')
    answer = input()
    
    # ユーザーの答えにより分岐
    if answer == "yes":
        low = guess + 1
    else:
        high = guess
        
print('あなたの考えている数字は', low, 'ですね！')