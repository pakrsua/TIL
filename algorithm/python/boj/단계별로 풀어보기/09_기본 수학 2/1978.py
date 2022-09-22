# 소수 찾기

N = int(input())
num = list(map(int,input().split()))

sosu = 0
for i in num:
    cnt = 0
    for j in range(1,i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        sosu += 1

print(sosu)