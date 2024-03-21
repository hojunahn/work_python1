name = "곱등이사육사" # 파이썬은 데이터형이 없기 때문에 값이 대입될 때 형이 결정 됨
age = 22
gender = '남성'
jobs = "소프트웨어 개발자"
addr = "경기도 수원시"
# C언어 스타일, %방식(서식을 지정하는 방식)
print("="*5,"스타일 지정 방식","="*5, sep="")
print("이름 : %s"%name)
print("나이 : %d, 성별 : %s"%(age,gender))
print("직업 : %s"%jobs)
print("주소 : %s"%addr)

# 파이썬 3.6 이전 스타일

print("===== 3.6 이전 스타일 =====")
print("이름 : {} \n주소 : {}".format(name,addr))
print("나이 : {}".format(age))



# 파이썬 현재 스타일
print("="*5,"파이썬 현재 스타일","="*5, sep="")
print(f"이름 : {name}")
print(f"성별 : {gender}, 직업 : {jobs}, 나이 : {age}")

# 자바 스타일 : + 연산자 사용
print("==== 자바 스타일 ====")
print("이름 : " + name)
print("나이 : " + str(age)) # 파이썬에서는 문자열로 변경해서 출력 (+)
print("성별 : " + gender)
print("주소 : " + addr)

# 출력 시 정렬
# < - 좌측 정렬
# < - 우측 정렬(기본값으로 생략 가능)
# ^ - 중앙 정렬

number = 125
number2 = 3.14592374747
print(f"|{number:5}|") # 5칸의 공간을 만들고 값을 오른쪽 정렬
print(f"|{number:<5}|") # 5칸의 공간을 만들고 값을 왼쪽 정렬
print(f"|{number:^5}|") # 5칸의 공간을 만들고 중앙 정렬
print(f"|{number2:.2f}|") # 실수값을 소수점 3번째 반올림해서 소수점 이하 2자리 출력