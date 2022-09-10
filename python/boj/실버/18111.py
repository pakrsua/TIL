# 18111 마인크래프트
import sys

n, m ,b = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

ans_time = 9876543210
ans_height = 0
end = 256
start = 0

# for h in range(257):
#     high = 0
#     low = 0
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] > h:
#                 high += (arr[i][j] - h)
#             else:
#                 low += (h - arr[i][j])
#     if low > high + b:
#         continue
#     # print('{} 층 답 {} {}'.format(h,time,h))
#
#     if (low + high * 2) <= ans_time:
#         ans_time = low + (high * 2)
#         ans_height = h
# print('{} {}'.format(ans_time, ans_height))
while end != start :
    time = 9876543210
    mid = (start + end) // 2
    mid_high = (mid + end) // 2
    mid_low = (start + mid) // 2

    high_high = 0
    high_low = 0

    low_high = 0
    low_low = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] > mid_high:
                high_high += (arr[i][j] - mid_high)
            elif arr[i][j] < mid_high:
                high_low += (mid_high - arr[i][j])
            elif arr[i][j] > mid_low:
                low_high += (arr[i][j] - mid_low)
            elif arr[i][j] < mid_low:
                low_high += (mid_low - arr[i][j])
    if high_low > b:
        end = mid
        continue
    if low_low > b:
        continue
    if low_low + (high_low * 2) < high_low + (high_high * 2):
        end = mid
        ans_time = low_low + (high_low * 2)
        ans_height = mid_low
    else:
        start = mid
        ans_time = high_low + (high_high * 2)
        ans_height = mid_high
print('{} {}'.format(ans_time, ans_height))