# 튜플 : 값을 변경할 수 없는 시퀸스 자료형(immutable)
# () 소괄호를 사용해서 만들거나 괄호가 없으면 튜플
person = 'Alice', 30, '곱등이사육사', True # Packing
print(person)

a,b,c,d = person # Unpacking
print(a)

# 튜플을 이용한 함수 반환 값 다루기
def get_person():
    name = "곱등이사육사"
    age = 25
    addr = "경기도 수원시"
    return name,age,addr

name_card = get_person()
print(name_card)