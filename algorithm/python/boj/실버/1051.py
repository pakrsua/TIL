# 1051 숫자 정사각형

N, M = map(int,input().split())

arr = [list(input()) for _ in range(N)]
if N > M:
    k = M
else:
    k = N
ans = 0
max_ans = 0
for i in range(N):
    for j in range(M):
        for a in range(k):
            if i+a < N and j+a < M and arr[i][j] == arr[i + a][j] == arr[i][j+a] == arr[i+a][j+a]:
                ans = (a + 1) * (a + 1)
                if ans > max_ans:
                    max_ans = ans
print(max_ans)