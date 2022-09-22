# 1012 유기농 배추

def bfs(arr,i,j):
    queue =

T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int,input().split())
    arr = [[0]*M for _ in range(N)]
    cnt += 1

    for i in range(K):
        x, y = map(int,input().split())
        arr[x][y] = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(arr,i,j)
                cnt += 1