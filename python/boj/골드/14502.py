# 14502. 연구소
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# 안전영역 계산하기
def safezone():
    global safe_cnt
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                safe_cnt += 1

# 바이러스 퍼뜨리기
def virus():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                for k in range(4):
                    nr = i + dc[k]
                    nc = j + dr[k]
                    if nr >= 0 and nc >=0 and nr < N and nc < M:
                        if arr[nr][nc] == 0:
                            arr[nr][nc] = 2
                            print(arr)
                            virus()

# 벽 3개 선택
def wall(cnt):
    # 기둥이 3개가 되면 바이러스 퍼뜨리기
    global ans
    if cnt >= 3:
        safe_cnt = 0
        virus()
        safezone()
        print(safe_cnt)
        if safe_cnt >= ans:
            ans = safe_cnt
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and visited[i][j] == 0:
                arr[i][j] = 1
                visited[i][j] = 1
                wall(cnt + 1)
                visited[i][j] = 0
                arr[i][j] = 0

N, M = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]


ans = 0
# print(arr)
wall(0)

print(ans)
