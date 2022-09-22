# 1916 최소비용 구하기
import heapq
import sys

def dijkstra(start):
    queue = []

    heapq.heappush(queue,[0, start])
    visited[start] = 0
    while queue:
        v, now = heapq.heappop(queue)
        # print(v, now)
        if visited[now] < v:
            continue
        for next in arr[now]:
            cost = v + next[1]
            if cost < visited[next[0]]:
                visited[next[0]] = cost
                heapq.heappush(queue,[cost,next[0]])

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = [[] for _ in range(N + 1)]
visited = [987654321] * (N + 1)
for i in range(M):
    start, end, cost = map(int,sys.stdin.readline().split())
    arr[start].append([end, cost])
start, end = map(int,sys.stdin.readline().split())
dijkstra(start)
print(visited[end])
