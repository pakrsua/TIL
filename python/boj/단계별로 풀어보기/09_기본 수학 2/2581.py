# 소수
M = int(input())
N = int(input())

add = 0
min = 10000
cnt = 0

for sosu in range(M, N+1):
    sosu_check = 0
    if sosu != 1:
        for i in range(2,sosu):
            if sosu % i == 0:
                sosu_check = -1
                break
        if sosu_check == 0:
            add += sosu
            cnt += 1
            if sosu < min:
                min = sosu
if cnt > 0:
    print(add)
    print(min)
else:
    print(-1)