# 별 찍기 - 2

N = int(input())

for i in range(1,N+1):
    print('',end=' '*(N-i))
    print('*'*i)