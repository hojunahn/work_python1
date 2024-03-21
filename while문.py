# while문 : 참인 동안 반복 수행,반복 횟수를 알수 없을때 주로
# 입력받은 정수의 합 구하기

# n = int(input("정수 입력: "))
# sum = 0;
# while n:
#     sum += n
#     n -= 1 # 자바 : n-- 파이썬은 안됨
# print(sum)

while True:
    age = int(input("나이 입력: "))
    if 0 <= age < 200: break
    print("나이 입력 범위를 벗어 났습니다.")