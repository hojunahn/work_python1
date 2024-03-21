# 문자열이 문자로 이루어진 데이터 집합, 파이썬은 문자를 별도로 다루지 않고 전부 문자열로 간주
# "한줄 문자열", '한줄 문자열', """ 여러줄 문자열 """, ''' 여러줄 문자열 '''
# 인덱싱이란 : 시퀀스 자료열(리스트, 튜플, 문자열)에서 특정 위치의 요소를 선택하는 작업, seq[index]
# 슬라이싱이란 : 시퀀스 자료형에서 일부분을 추출, seq[start:end:step]
my_list = [0,1,2,3,4,5,6,7,8,9] # 리스트 생성 []
slice_without_step = my_list[2:7] # 인덱스는 0부터 시작, end는 미만
slice_without_step = my_list[1:9:2] # 1,3,5,7

# 인덱싱, 슬라이싱 실습
# 주민등록번호 자르기, 하위 7자리중 첫번째 글자는 성별, 앞에 6자리는 년,월,일

jumin = "991120-1234567"
print("성별 : " + jumin[7])
print("년 : " + jumin[:2]) # 0부터 2미만
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:]) # 7에서 끝까지
print("뒤 7자리 : " + jumin[-7:])

python_str = "Life is too short, You need Python"
new_str = python_str[0] + python_str[1] + python_str[2] + python_str[3]
# python_str[0] = "l" # 리터럴 상수이기 때문에 변경 안됨
print(new_str)

# 대소문자 바꾸기 : upper(), lower()
print(python_str.upper())
print(python_str.lower())

# 문자열 변경
a_str2 = "Hello Python Program"
new_str2 = a_str2.replace("Python","JavaScript")
print(new_str2)
# 문자열에 포함된 문자 갯수 세기(count()), 문자열 길이(len(), __len__())
print(a_str2.count("l")) # 해당 문자열에서 count()함수의 전달 문자가 몇개 존재하는지 반환
print(len(a_str2)) # 문자열 길이를 반환하는 함수
print(a_str2.__len__()) # 문자열 길이를 반환하는 내장 함수

# 문자열 찾기
# find() : 찾은 인덱스 반환, 없으면 -1 ,
# rfind() : 뒤에서 부터 문자열 찾고 찾은 인덱스는 앞에서 부터 계산
# index() 찾은 문자열의 인덱스 반환, 없으면 ValueError
phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장"))
print(phrase.rfind("가장"))
print(phrase.index("포기"))
print(phrase.find("나에게"))
# print(phrase.index("나에게"))
new_str = phrase.replace("가장","나에게") # 입력한 문자가 위치한 자리에 다른 문자넣기
print(new_str)
# 문자열 연산자 : "문자열" + "문자열", "문자열"*3
print("태양고" + "나희도")
print("태양고" * 2)
# print("태양고" + 2) # 이건 안됨
# 문자열 양옆의 공백 제거 : strip()
input_a = """
     안녕하세요.
    문자열 함수를 알아 봅니다.

"""
print(input_a.strip())