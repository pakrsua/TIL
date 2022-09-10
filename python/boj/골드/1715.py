# 1715 카드 정렬하기

import heapq

n = int(input())
arr = []
for i in range(n):
    heapq.heappush(arr, int(input()))

print(arr)

if n == 1:
    print(0)
else:
    ans = 0
    while len(arr) > 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        ans += a + b
        heapq.heappush(arr, a + b)
    print(ans)