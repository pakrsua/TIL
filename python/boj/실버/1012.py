# 1012 유기농 배추
# 재귀 깊이 연장
import sys
sys.setrecursionlimit(10 ** 6)

# 상하좌우
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

#재귀 함수
def find(x, y):
    for k in range(4):
# 상하좌우의 배추 찾기
        nr = x + dr[k]
        nc = y + dc[k]

        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 1:
                arr[nr][nc] = 2
                find(nr, nc)

#입력부분
T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())
    cnt = 0

    arr = [[0] * M for _ in range(N)]
# 문제에서 주어진 밭 만들기
    for kc in range(K):
        y, x = map(int, input().split())
        arr[x][y] = 1

    # print(arr)
    for j in range(M):
        for i in range(N):
            if arr[i][j] == 1:
                find(i, j)
# 카운드 증가
                cnt += 1
    print(cnt)