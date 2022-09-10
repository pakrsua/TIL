# 9461 파도반 수열

T = int(input())

for tc in range(T):
    N = int(input())
    P = [0] * (N + 3)
    P[0] = 1
    P[1] = 1
    P[2] = 1

    for i in range(3, N):
        P[i] = P[i - 3] + P[i - 2]
        # print(P)
    print(P[N - 1])