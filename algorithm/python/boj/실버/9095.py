# 9095 1, 2, 3 더하기

T = int(input())

for tc in range(T):
    n = int(input())
    N = [0] * (n + 3)
    N[1] = 1
    N[2] = 2
    N[3] = 4

    for i in range(4, n+1):
        N[i] = N[i - 1] + N[i - 2] + N[i - 3]

    print(N[n])

