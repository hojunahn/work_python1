a, b, c = map(int, input("정수 3개 입력 : ").split())
ls = str(a * b * c)
duplicates = {}  # 중복된 숫자와 그 등장 횟수를 저장할 딕셔너리

for i in range(10):
    count = ls.count(str(i))  # 각 숫자의 등장 횟수를 세기
    if count > 1:  # 등장 횟수가 1보다 크면 중복된 숫자로 간주
        duplicates[i] = count
    else:
        duplicates[i] = count

print("숫자:중복 :", duplicates)

# 범위를 지정하지 않고 a,b,c 각각의 정수에서 제일 큰수를 기준으로 지정함

a, b, c = map(int, input("정수 3개 입력 : ").split())
ls = str(a * b * c)
duplicates = {}  # 중복된 숫자와 그 등장 횟수를 저장할 딕셔너리

# 입력받은 수까지 반복하여 중복된 숫자와 등장 횟수를 저장
for i in range(max(a, b, c) + 1):
    count = ls.count(str(i))  # 각 숫자의 등장 횟수를 세기
    if count > 1:  # 등장 횟수가 1보다 크면 중복된 숫자로 간주
        duplicates[i] = count

print("숫자:중복 :", duplicates)