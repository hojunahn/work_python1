# 무작위 수를 공백으로 기준하여
# 입력 받아 홀수와 짝수로 리스트에 나누어 담아 출력 하는 문제 입니다.

# number = list(map(int, input().split())) # map(함수, 리스트)
# even = []
# odd = []
#
# for e in number: # 리스트의 요소를 시작부터 끝까지 순회
#     if e % 2 == 0: even.append(e)
#     else: odd.append(e)
# print(f"홀수: {odd} 짝수: {even}")

num = list(map(int, input().split()))
even = list(filter(lambda x:x % 2 == 0, num))
odd = list(filter(lambda x:x % 2 == 1, num))
print(f"홀수 : {odd}, 짝수 : {even}")