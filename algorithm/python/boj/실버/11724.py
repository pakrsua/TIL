# 11724 연결 요소의 개수
import sys
sys.setrecursionlimit(10**6)

def dfs(n):
    for i in range(len(arr[n])):
        if visited[arr[n][i]] == 0:
            visited[arr[n][i]] = 1
            dfs(arr[n][i])

N, M = map(int,input().split())
arr = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
ans = 0
for m in range(M):
    u,v = map(int,sys.stdin.readline().rstrip().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(1, N+1):
    if visited[i] == 0:
        visited[i] = 1
        dfs(i)
        ans += 1
print(ans)
