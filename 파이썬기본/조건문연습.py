n = int(input("정수 입력: "))
a = n // 100 # 100 나눈 몫
b = (n % 100) // 10 # 100으로 나눈 나머지에서 10으로 나눈 몫
c = n % 10 # 10으로 나눈 나머지

if a > b:
    if a > c: print(a)
    else: print(c)
else:
    if b > c: print(b)
    else: print(c)

