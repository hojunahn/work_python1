# for문에서 contionue 사용
# n = int(input("정수 입력: "))
# for i in range(n):
#     if i % 2 == 0: continue
#     print(i,end=" ")

# for문을 반대로 반복하기
# for i in range(10, 0-1, -1): # 초기값 10, 종료값 0(미만이기 때문에 -1),증감값 -1(10에서 부터 1씩 감소 0까지 반복)
#     print(f"index : {i}")

# for문을 알파벳 출력하기 :
# chr(유니코드 값을 입력 받아 문자출력)
# ord(문자의 유니코드 값을 반환)
for i in range(ord("A"), ord("Z")+1):
    print(chr(i),end=" ")
print()

for i in range(65, 91): # A : 65, Z : 90
    print(chr(i),end=" ")
print()