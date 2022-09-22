# 2178. 미로 탐색
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def BFS(r,c):
    global visited
    queue = [arr[r][c]]
    visited[r][c] = 1

    while queue:
        r, c = queue.pop(0)
        if r == N-1 and c == M-1:
            print(arr[r][c])
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == 0 and arr[nc][nr] == '1':
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append(nr,nc)


N, M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
BFS(0, 0)