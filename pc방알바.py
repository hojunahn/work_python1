
seat_lists = [[] for _ in range(100)]
n = int(input("손님 수: "))
person_seat = list(map(int,input("오신 순서대로 자리 입력: ").split()))

rep = 0
for seat_number in person_seat:
    if seat_lists[seat_number-1]:
        print("자리에 손님이 계시네요 다른데 가실?")
        rep+=1
    else:
        seat_lists[seat_number-1].append(seat_number)
print("거절당한 횟수: ",rep)
print(f"현재 자리 : {seat_lists}")