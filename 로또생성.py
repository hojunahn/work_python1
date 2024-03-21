import random

# 1 ~ 45까지의 로또 번호 6개를 찾기
lotto_number = []

for i in range(0,46):
    if i not in lotto_number:
        lotto_number.append(i)
random_smp = random.sample(lotto_number,6)
print(random_smp)





