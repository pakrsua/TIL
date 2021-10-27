# 1753 최단경로

def check(st):
    global visited
    q=[0]
    q.append(st)
    visited[st] = 0

    while q:
        dist = q.pop(0)
        now = q.pop(0)
        if visited[now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]
            if cost < visited[i[0]]:
                visited[i[0]] = cost
                q.append(cost)
                q.append(i[0])
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