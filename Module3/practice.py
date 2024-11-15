# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」

secret_num = 88

while True:
    print("請輸入想猜的數字(1~100)")
    num = int(input())
    if num == secret_num:
        print("恭喜中獎")
        break
    elif 100 > num > secret_num:
        print("數字要在小一點喔")
    elif 1 < num < secret_num:
        print("數字要在大一點喔")
    elif num > 100 or num < 1:
        print("數字在1~100中間喔")
















