# for문 : 정해진 범위 만큼 반복할 때 주로 사용
# for 요소 in 시퀀스: 시퀀스는 리스트, 튜플, 문자열 들을 의미, 자바의 향상된 for문과 유사

# fruits = ["사과", "바나나", "딸기", "수박", "참외", "복숭아"]
#
# for e in fruits:
#     print(e, end="\n")

# for 변수 in range(시작,종료,증감): 자바의 일반적인 for문과 유사

# n = int(input("정수 입력: "))
# sum = 0
#
# for i in range(1,n+1): # 즉감값은 생략하면 1씩증가
#     sum+=i
# print(sum)

# 이중 for문 사용

# n = int(input("정수 입력 : "))
#
# for i in range(0,n):
#     for j in range(0,n):
#         print("*",end=" ")
#     print()

# 구구단 출력

# for i in range(2,10):
#     print(f"========== {i}단 ==========")
#     for j in range(1,10):
#         print(f"===={i}*{j} = {i*j}")


# 이중 for문과 조건문 사용

n = int(input("정수를 입력 하세요 : "))
for i in range(0,n):
    for j in range(0,n):
        if j % 2 == 0:
            print(">", end="")
        else:
            print("<", end=" ")
    print()