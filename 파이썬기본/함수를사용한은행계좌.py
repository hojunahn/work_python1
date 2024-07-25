# 계좌 개설
ls = []
ls1 = 0
def open_account(name): # 매개변수와 반환값이 있는 함수 선언
    print(f"{name}님의 계좌가 개설 되었습니다.")
    return name
def deposit(input): # 잔액과 입금액을 매개변수로 전달 받음 (입금)
    global balance
    balance+=input
    print(f"{input}이 입금되었습니다. 잔액은 {balance + input}입니다.")

def withdraw(input):
    global balance
    if balance >= input:
        balance -= input
        print(f"{input}이 출금되었습니다. 잔액은 {balance}입니다.")
    else:
        print(f"출금이 실패했습니다. 잔액은 {balance}입니다.")

balance = 0 # 현재 잔액을 외부에서 선언
name = open_account("곱등이사육사")
balance = deposit(1000)
balance = withdraw(500)
print(f"{name}님의 잔액은 {balance} 입니다.")

print(ls1)