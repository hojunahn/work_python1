# 1 ~ 45까지의 로또 번호 6개를 자동 생성하기, 중복 제거
import random
ls = [] # 빈 리스트 생성
while True: # 반복 횟수를 알수 없기 때문에 True, 반드시 탈출조건 필요
    rand = random.randrange(1,46) # 1에서 46미만(45), 임의의 값 생성
    if rand not in ls:
        ls.append(rand)
    if len(ls) == 6: break
print(ls)