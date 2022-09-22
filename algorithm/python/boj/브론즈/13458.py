# 13458 시험 감독

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = N

for n in range(N):
    A[n] -= B

    if A[n] > 0:
        cnt += A[n] // C
        if A[n] % C > 0:
            cnt += 1
print(cnt)