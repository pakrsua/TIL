#14890 경사로

# def check(grond):
#     visited = [[0] * N for _ in range(N)]
#     for i in range(N-1):
#         if grond

N, L = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cnt = 0

for i in range(N-1):
    for j in range(N-1):
        if arr[i][j]