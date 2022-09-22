# 소수구하기

M, N = map(int, input().split())

for i in range(M,N+1):
    sosu_check = 1
    if i != 1:
        for j in range(2,int(i**(0.5))+1):
            if i > 2:
                if i % j == 0:
                    sosu_check = 0
                    break
        if sosu_check == 1:
            print(i)