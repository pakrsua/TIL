# 15685 드래곤 커브

# 우 상 좌 하
dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]
arr = [[0] * 101 for _ in range(101)]
move = []

n = int(input())

for tc in range(n):
    move = []
    x, y, d, g = map(int, input().split())
    move.append(d)
    arr[x][y] = 1
    # 방향받기
    for i in range(g):
        temp = []
        temp.extend(move)
        temp.reverse()
        for j in range(len(temp)):
            temp[j] = (temp[j] + 1) % 4
            move.append(temp[j])
    # 점 찍기
    for i in range(len(move)):
        nr = x + dr[move[i]]
        nc = y + dc[move[i]]
        arr[nr][nc] = 1
        x, y = nr, nc

ans = 0
for i in range(100):
    for j in range(100):
        if arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1] and arr[i][j]:
            ans += 1
print(ans)
