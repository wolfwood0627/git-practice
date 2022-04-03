# 300以下のフィボナッチ数列を奇数のみ表示
a = 0
b = 1

while a <= 300:
    print(a)
    a, b = b, a+b
