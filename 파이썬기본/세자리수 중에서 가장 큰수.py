num = list(map(int,input("3자리 정수 입력: ")))
if len(num) != 3:
    print("세 자리 정수 입력")
else:
    num1 = num[0]
    num2 = num[1]
    num3 = num[2]

    num_max = 0
    if num1 > num2 and num1 > num3:
        num_max = num1
    elif num2 > num1 and num2 > num3:
        num_max = num2
    else:
        num_max = num3

    print(f"세자리 수 중에서 가장큰수는 {num_max}입니다.")