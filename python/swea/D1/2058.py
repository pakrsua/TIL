# 2058 자릿수 더하기

N = int(input())

add = 0

while N > 0:
    add += N%10
    N = N//10

print(add)