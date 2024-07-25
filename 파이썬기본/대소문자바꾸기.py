# 문자열을 입력 받아 대문자는 소문자로, 소문자는 대문자로 변경하기
# rst = ""
# for e in input("단어 입력: "):
#     if e.islower():
#         rst += e.upper()
#     else:
#         rst += e.lower()
# print(rst)

# a = int(input("a정수: "))
# b = int(input("b정수: "))
# c = int(input("c정수: "))
# mul_num = a*b*c
# mul_str = str(mul_num)
# arr = []
# dp = set()
# z = 0
# pz = ""
# asz = 0
# for i in mul_str:
#     arr+=i
#     asz+=arr.count(i)
# print(asz)
#     if mul_str.count(i)>1:
#         z+=dp.add(i)
#
# print(list(z))


a = int(input("a정수: "))
b = int(input("b정수: "))
c = int(input("c정수: "))
ls = str(a*b*c)
for i in range(10):
    print(ls.count(str(i)))

