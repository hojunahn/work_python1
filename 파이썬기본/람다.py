# 람다(lambda) : 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현 한 것
# 람다는 주로 이름없는 함수를 만들 때 사용
# 람다 장점은 코드의 간결함, 메모리 절약 등의 이점이 있음
# def add(a, b):
#     return a + b
# print(add(10,20))
# print((lambda a,b: a + b), (10, 20))

# 함수의 매개변수로 함수 전달 하기
def call_times(func):
    for i in range(10):
        func()

def print_hello():
    print("HELLO!!")

# call_times(print_hello)


def power(n):  # 입력값의 제곱을 구하는 함수
    return n * n
power2 = lambda n:n * n # 입력값의 제곱을 구하는 람다식

input = map(int, input().split())
rst = list(map(lambda n:n * n, input))
print(rst)