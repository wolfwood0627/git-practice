# 300以下のフィボナッチ数列を奇数のみ表示
a = 0
b = 1

while a <= 300:
    a, b = b, a+b
    if a % 2 == 0:
        countinue
    print(a)
    a, b = b, a+b
    
    
