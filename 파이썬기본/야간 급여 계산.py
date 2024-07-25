work = int(input("주간근무[1], 야간근무[2] 선택 : "))
work_time = int(input("근무 시간 입력: "))
pay = 0
work_money = 9620
if work == 1:
    pay = work_money * work_time
    print(f"입력한 시간 동안 근무한 주간 급여는 {pay}원 입니다.")
elif work == 2:
    pay = (work_money * 1.5)*work_time
    print(f"입력한 시간 동안 근무한 야간 급여는 {pay}원 입니다.")
