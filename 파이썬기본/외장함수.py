# 외장 함수 : 파이썬의 표준 모듈이지만 import해야 사용 가능
# import random
# for i in range(10):
#     # rand = random.randint(0, 4)  # 0 ~ 4사이의 임의 의 정수 반환(4가 포함)
#     # rand = random.randrange(0, 4)  # 0 ~ 4 미만
#     rand = random.randrange(4) # 0 ~ 4 미만
#     print(rand)

# 날짜 및 시간 관련 처리 모듈
# from datetime import datetime  # datetime 모듈에서 datetime 함수만 import
# datetime.today()
# print(datetime.today().year,"년")  # 현재 연도 가져 오기
# print(datetime.today().month,"월") # 현재 월 가져 오기
# print(datetime.today().day,"일") # 현재 일 가져 오기
# print(datetime.today().hour,"시") # 현재 시간 가져 오기
# print(datetime.today().minute,"븐") # 현재 분 가져 오기
# print(datetime.today().second,"초") # 현재 초 가져 오기

# 달력 생성
import calendar
# print(calendar.calendar(2024))
# print(calendar.calendar(2024,m=5))
# print(calendar.month(2024,3))

# math 모듈
import math
print(math.sin(100))
print(math.cos(100))
print(math.tan(100))
print(math.ceil(1.0000001))
print(math.floor(1.0000001))