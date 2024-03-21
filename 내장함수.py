# # 내장 함수 : 별도의 import 없이 사용할 수 있도록 내장된 함수를 말함
print(max(32,100,45,79,12,6,97))
print(min(32,100,45,79,12,6,97))

print(sum([26, 34, 45, 67, 78])) # sum에는 리스트 혹은 튜플 형태로 전달 [],()

value = 1,2,3,4,5,6,7,8,9,0
print(sum(value))
print(f"평균 : {sum(value)/len(value)}")

print(divmod(sum(value),4)) # 몫과 나머지


