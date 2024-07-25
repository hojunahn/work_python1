import numpy as np # 넘파이 모듈을 가져오고 별칭을 np로 정함
# 배열이란? 순서가 있는 같은 종류의 데이터가 저장된 집합을 의미

data = [1,2,3,4,5,6,7] # 리스트 생성
# data2 = (1,2,3,4,5,6,7) # 튜플
# data3 = 1,2,3,4,5,6,7 # 튜플
# data4 = 1, # 튜플

print(type(data))
# print(type(data2))
# print(type(data3))
# print(type(data4))

a1 = np.array((data)) # 리스트를 넘파이 배열로 변환

print(a1)
print(data)

data2 = [0,1,3,4,0.5,3.14,9.99] # 리스트는 데이터 형이 달라도 입력 가능
a2 = np.array(data2) # 넘파이 배열은 다른 같은 타입이어야 하므로 자동 형변환이 일어 남
print(a2)

x = np.array([0.1,0.2,0.3])

print(x)
print(x.shape) # 배열의 형태를 나타냄
print(x.dtype) # 배열 요소의 데이터 타입을 반환

y = np.array(([1,2,3], [4,5,6]))
print(y)
print(y.shape)
print(y.dtype)

# 범위를 지정해 배열 생성 : arange()
a3 = np.arange(0,10,2) # 0 ~ 10 미만, 간격은 2씩 증가, 생략하면 기본값은 1
print(a3)

# 배열의 형태 변경
a4 = np.arange(12).reshape(4, 3) # 0 ~ 12 미만의 배열을 생성하고, 배열의 구조를 4 * 3
print(a4)

# 범위의 시작과 끝, 그리고 범위를 지정하는 메소드 : linspace()
a5 = np.linspace(1, 10, 6)
print(a5)

# 0 ~ 파이값까지 동일한 간격으로 20개 데이터 생성
a6 = np.linspace(0, np.pi, 20)
print(a6)

# 특별한 형태의 배열 생성
a7 = np.zeros(10) # 0으로 초기화된 10개의 배열 생성
print(a7)

a8 = np.zeros((3,4)) # 0으로 초기화된 2차원(3*4)배열 생성
print(a8)

a9 = np.ones(10)
print(a9)

a10 = np.ones((3,4))
print(a10)

# 단위 행렬 만들기 : n * n인 정사각형의 행렬의 주대각선이 모두 1이고 나머지는 0인 행렬
a11 = np.eye(4)
print(a11)

# 배열의 데이터 타입 변환
a12 = np.array(['1.5','0.62','2','3.14','3.141592'])
print(a12)
print(a12.dtype) # U8은 유니코드를 의미 함

num_a12 = a12.astype(float) # 주어진 문자열 실수 타입으로 변환
print(num_a12)

a14 = np.array(['1', '3', '5', '7', '9'])
num_a14 = a14.astype(int) # 문자열을 정수 타입으로 변환
print(num_a14)


# 난수 배열 생성하기
a14 = np.random.rand(2, 3) # 0 ~ 1 미만의 임의의 실수값을 생성, 2*3
print(a14)
a15 = np.random.rand(2,3,4)
print(a15)

# 지정한 범위에 해당하는 정수로 난수 배열을 생성
a16 = np.random.randint(10, size=(3,4))
print(a16)

# 배열의 연산 : 배열은 다양한(+, -, *, /) 연산을 할수 있음. 단 배열의 형태(shape)가
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr2 / arr1)

# 요소별 비교 연산
arr3 = np.array([10,20,30,40,50])
print(arr3 > 20) # True와 False 반환

# 통계를 위한 연산 : 배열의 합, 표준 편차, 분산, 최대값과 최솟 값을 누적합과 누적
# 통계에서 많이 사용하는 메소드를 제공 해줌
arr4 = np.arange(5) # 0 ~ 5 미만의 값 생성
print(arr4)
print(f"합계 : {arr4.sum()}")
print(f"평균 : {arr4.mean()}")
print(f"표준편차 : {arr4.std()}")
print(f"분산 : {arr4.var()}")
print(f"최소값 : {arr4.min()}")
print(f"최대값 : {arr4.max()}")

# 배열의 인덱싱 / 슬라이싱
arr5 = np.array([1,2,3,4,5])
# 인덱싱
print(arr5[3]) # 4번째 인덱스의 값 : 인덱스는 0부터 시작
# 슬라이싱
print(arr5[:4]) # 0번째 인덱스 부터 4번 인덱스 미만 까지 값을 잘라냄

#
arr6 = np.array([1,2,3,4,5])
arr7 = np.arange(6,11)
print("add : ", np.add(arr6, arr7))
print("sub : ", np.subtract(arr6, arr7))
print("mul : ", np.multiply(arr6, arr7))
print("div : ", np.divide(arr6, arr7))
print("pow : ", np.power(arr6, arr7))

# 행렬 연산 : 행렬간의 연산, 다차원 배열 대해서~
matrix1 = np.array([[1,2], [3,4]])
matrix2 = np.array([[5,6], [7,8]])

# 행렬 덧셈
print("="*5, "다차원행렬 연산", "="*5)
print(np.add(matrix1, matrix2))
print(np.subtract(matrix2, matrix1))
print(np.multiply(matrix1, matrix2))

# 전치 행렬 : 행과 열을 교환하여 얻어진 행렬
matrix3 = np.array([[1,2], [3,4]])
inverse_matrix = np.linalg.inv(matrix3)
print(inverse_matrix)

# 정렬과 탐색
x_sort = np.array([9,8,7,12,13,2,1,5])
print(np.amin(x)) # 최소값
print(np.amax(x)) # 최대값
print(np.argmin(x)) # 최소값이 있는 위치
print(np.argmax(x)) # 최대값이 있는 위치
print(np.sort(x)) # 오름차순 정렬
print(np.argsort(x)) # 값의 인덱스

# 브로드캐스팅 : 배열의 크기가 다른 경우에
print("----------------- 브로드 케스팅 연산-----------------")
a = np.array([1, 2, 3]) # 1차원 배열
b = np.array([[4], [5], [6]]) # 2차원 배열 (3 X 1)

# 브로드캐스팅을 사용한 배열 연산
c = a + b

print(c)