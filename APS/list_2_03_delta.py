## 델타 연습문제_1
## 달팽이 숫자


# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
# #
# N = int(input())
#
# arr = [[0] * N for _ in range(N)]
#
# d = 0  # 방향
# r = 0  # 행
# c = 0  # 열
# num = 1
#
# while num <= N * N:
#     arr[r][c] = num
#     num += 1
#
#
#     nr = r + dr[d]
#     nc = c + dc[d]
#
#     if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
#         r, c = nr, nc
#     else:
#         d = (d + 1) % 4
#         r += dr[d]
#         c += dc[d]
#
# for i in range(N):
#     for j in range(N):
#         print(arr[i][j], end=' ')
#     print()

##############################################################################
# 델타로 함수 탐색

arr = [
    [0, 1, 2, 3], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]
]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1] # 상하좌우
