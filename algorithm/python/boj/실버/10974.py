# 10974 모든 순열
# def arr(n):
#     global ans
#     if n == N:
#         print(*visited)
#     else:
#         for i in range(N):
#             if visited[i] == 0:
#                 visited[i] = n+1
#                 arr(n+1)
#                 visited[i] = 0
#
# N = int(input())
# visited = [0] * N
# ans = []
# arr(0)

def arr(depth):
    global ans

    if depth == n:
        print(*visited)
    else:
        for i in range(n):
            if i + 1 in visited:
                continue
            visited[depth] = i + 1
            arr(depth + 1)
            visited[depth] = 0
n = int(input())
visited = [0] * n
arr(0)