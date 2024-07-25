# 3개의 정수를 입력 받아 최대값/최소값 구하기
from datetime import datetime

# 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기

# 2개의 문자열을 변수 s와 k에,
# 양의 정수를 변수 n에 각각 전달 받아 s문자열의 뒤 부분의 n개의 문자를 k문자열 앞에 끼워 넣는 코드 작성
# 예)
# s : seoul
# k : korea
# n : 2
# result : ulkorea

# number = list(map(int,input("정수 3개 입력 : ").split()))
#
# print("최대값 : {} 최소값 : {}".format(max(number),min(number)))


# jumin = input("주민번호 입력 : ")
# today = datetime.today().year
# age = 0
# gender_str = ""
# year = int(jumin[:2])
# month = int(jumin[2:4])
# day = int(jumin[4:6])
# jender = int(jumin[7])
#
# if jender == 3 or jender == 4:
#     age = today - 2000 - year
# elif jender == 1 or jender == 2:
#     age = today - 1900 - year
#
# if jender == 1 or jender == 3:
#     gender_str = "남성"
# elif jender == 2 or jender == 4:
#     gender_str = "여성"
#
# print(f"{year:02}년 {month:02}월 {day:02}일")
# print(f"성별 : {gender_str}")
# print(f"나이 : {age}")

# s = input("s 문자열 : ")
# k = input("k 문자열 : ")
# n = int(input("정수 입력 : "))
#
# print(s[-n:] + k)

# 여러개의 정수를 입력 받아 합계와 평균 구하기
num2 = list(map(int,input("정수 여러개 : ").split()))

print(f"합계 : {sum(num2)} 평균 : {sum(num2)/len(num2)}")