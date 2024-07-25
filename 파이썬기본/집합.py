# 집합 자료형은 주로 중복 제거용 으로 사용
# 순서를 보장하지 않음
# 중복 불가
# mutable(Read / Write 가능)

# s1 = set([1,2,3,4,5])
# s2 = set([4,5,6,7,8])
# s3 = s1.union(s2) # 합집합, 중복 제거 (합집합의 다른 식:s3 = s1 | s2)
# s4 = s1.intersection(s2) # 교집합 (교집합의 다른 식:s3 = s1 & s2)
# s5 = s1.difference(s2) # 차집합 (차집합의 다른 식:s3 = s1 - s2)
# print(s3,s4,s5)

import random
lotto = set()
while True:
    num = random.randrange(1,46)
    lotto.add(num)
    if len(lotto) == 6: break
print(lotto)
