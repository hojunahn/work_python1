# 파이썬은 변수 선언 시 데이터 타입을 지정하지 않으며, 변수에 값이 대입 될때 형이 결정 됨
number = 200
str = ""
print(type(number)) # type() : 변수의 데이터형을 확인
print(type(str))
print(type(bool))
# print(type(number2))

# 형변환 : 선언된 변수에 값이 할당되는 순간 형이 결정, 다른 데이터형으로 변경 할 때 사용
print(10 + int("10"))
print("나이 : " + str(30))

var = "" # 공백은 거짓
number = None # 0은 거짓
print(bool(number)) # boolean 값의 거짓 : "",0,False,None