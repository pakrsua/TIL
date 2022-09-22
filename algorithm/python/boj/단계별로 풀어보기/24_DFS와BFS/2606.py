# 2606. 바이러스

# DFS로 문제 풀어보기

def DFS(n):
    global visited, cnt
    visited[n] = 1
    for i in range(len(arr[n])):
        if arr[n][i] == 1:
            if visited[i] == 0:
                cnt += 1
                DFS(i)

computer = int(input())
connect = int(input())
visited = [0]*(computer+1)
arr = [[0]*(computer+1) for _ in range(computer+1)]
cnt = 0
for con in range(connect):
    st, ed = map(int,input().split())
    arr[st][ed] = 1
    arr[ed][st] = 1

DFS(1)
print(cnt)