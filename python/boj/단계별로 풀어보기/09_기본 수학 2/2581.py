# 소수
M = int(input())
N = int(input())

add = 0
min = 10000
cnt = 0

for sosu in range(M, N+1):
    sosu_check = 0
    for i in range(1,sosu+1):
        if sosu % i == 0:
            sosu_check += 1
    if sosu_check == 2:
        add += sosu
        cnt += 1
        if sosu < min:
            min = sosu
if cnt > 0:
    print(add)
    print(min)
else:
    print(-1)