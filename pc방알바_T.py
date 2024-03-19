person = int(input())
num = list(map(int,input().split()))
pc = [0]*100
cnt = 0
for e in num:
    if pc[e - 1] != 0: cnt +=1
    else:pc[e - 1] = 1
print(cnt)