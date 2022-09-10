# 15683 감시

def cctv(num):
    # 방향 정하고 채우기
    if(num == 1):
        for d in range(4):
            nr = i + dr[d]
            nc = j + dc[d]
            if nr < N and nr > 0 and nc < M and nc > 0:
                arr[nr][nc] = '#'
    if(num == 2):
        for d in range(4):
            nr = i + dr[d]
            nc = j + dc[d]
            if nr < N and nr > 0 and nc < M and nc > 0:
                arr[nr][nc] = '#'
            bnr = i - dr[d]
            bnc = j - dc[d]
            if bnr < N and bnr > 0 and bnc < M and bnc > 0:
                arr[bnr][bnc] = '#'
    if(num == 3):
        for d in range(4):
            nr = i + dr[d]
            nc = j + dc[d]
            if nr < N and nr > 0 and nc < M and nc > 0:
                arr[nr][nc] = '#'
            if d < 3:
                nnr = i + dr[d+2]
                nnc = j + dc[d+2]
                if nnr < N and nnr > 0 and nnc < N and nnr > 0:
                    arr[nnr][nnc] = '#'
            else:
                nnr = i + dr[0]
                nnc = j + dc[0]
                if nnr < N and nnr > 0 and nnc < N and nnr > 0:
                    arr[nnr][nnc] = '#'
    if(num == 4):
        for d in range(4):
            nr = i + dr[d]
            nc = j + dc[d]
            if nr < N and nr > 0 and nc < M and nc > 0:
                arr[nr][nc] = '#'


# 사각지대 검사
def check():
    global min_cnt
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1

# 상우하좌
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

# 사무실 입력받기
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cctv = []
check = [[0] * M for _ in range(N)]

min_cnt = 987654321

for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != 6:
            check[i][j] = 1
            cctv(i, j, arr[i][j])

