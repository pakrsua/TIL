# 1260. BFS와 DFS

def DFS(v):
    global visited
    # 들어온 수를 방문체크 해준다
    visited[v] = 1
    # 현재 탐색하는 수를 출력한다
    print(v, end=' ')
    # 연결된 다른 노드 확인
    for i in range(len(arr[v])):
        # 해당 노드가 연결되어있고,
        if arr[v][i] == 1:
            # 방문체크가 되어있지 않다면
            if visited[i] == 0:
                # 해당 노드로 이동
                DFS(i)

def BFS(v):
    global visited
    # queue를 만들어준다
    Q = [v]
    # 방문 체크
    visited[v] = 1
    # queue에 값이 존재하는 동안 반복
    while Q:
        # 현재 탐색하는 수는 Q리스트 안의 가장 앞의 값
        v = Q.pop(0)
        print(v, end=' ')
        for i in range(1, N+1):
            # 방문체크가 안되어있고 현재 탐색중인 노드와 연결되어 있다면
            if visited[i] == 0 and arr[v][i] == 1:
                # Q리스트에 넣어준다
                Q.append(i)
                # 방문 체크
                visited[i] = 1

N, M, V = map(int,input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)

for num in range(M):
    st, ed = map(int, input().split())
    # '양방향'이기 때문에 두가지 경우를 모두 연결시킨다.
    arr[st][ed] = 1 # 단방향일 경우 이 코드만 써도 된다
    arr[ed][st] = 1
DFS(V)
print()
visited = [0]*(N+1)
BFS(V)

