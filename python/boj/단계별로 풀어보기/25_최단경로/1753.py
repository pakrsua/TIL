# 1753 최단경로
import heapq
# 시간초과
def check(st):
    global visited
    q=[]
    heapq.heappush(q, (0,st))
    visited[st] = 0

    while q:
        dist, now = heapq.heappop(q)
        if visited[now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]
            if cost < visited[i[0]]:
                visited[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    # print(visited)

V, E = map(int,input().split())
start = int(input())
arr = [[]* (V+1) for i in range(V+1)]


for line in range(E):
    u, v, w = map(int,input().split())
    arr[u].append((v,w))

cnt = 0
visited = [9876543210] * (V + 1)
check(start)

for ans in range(1, V+1):
    if visited[ans] == 9876543210:
        print('INF')
    else:
        print(visited[ans])

#잘못품
# def find_set(x):
#     if p[x] != x:
#         p[x] = find_set(p[x])
#
# def union(x, y):
#     p[find_set(y)] = find_set(x)
#
# V, E = map(int,input().split())
# K = int(input())
# line = []
# p = [0] * (V)
#
# for tc in range(E):
#     u, v, w = map(int,input().split())
#     line.append([u,v,w])
#
# line.sort(key=lambda x:x[2])
# for i in range(1, V+1):
#     p[i-1] = i
#
# ans = 0
# idx = 0
# pick = 0
#
# while pick < V-1:
#     x = line[idx][0]
#     y = line[idx][1]
#
#     if find_set(x) != find_set(y):
#         union(x,y)
#         pick += 1
#         ans = line[idx][2]
#     idx += 1
#
# print()