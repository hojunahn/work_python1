# 임의의 수를 연속(공백)으로 입력 받아 홀수, 짝수 리스트로 나누어 담기
# 1 2 3 4 5 6 7 8 9 10
# 홀수 : ~
# 짝수 : ~

land_num = list(map(int,input("수 입력 : ").split()))
odd_num = []
even_num = []
for i in land_num:
    if i % 2 == 0:
        even_num.append(i)
    else:
        odd_num.append(i)
print(f"홀수: {sorted(odd_num)} 짝수: {sorted(even_num)}")