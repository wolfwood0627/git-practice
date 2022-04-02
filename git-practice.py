# 100以下のフィボナッチ数列を表示
a = 0
b = 1
while b < 300:
    a, b = b, a+b
    # 偶数の場合表示させない
    if b % 2 == 0:
        continue
    print(b)
    
    
