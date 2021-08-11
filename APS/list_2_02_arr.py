##배열 순회##

N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

#행 우선 순회
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j])
#출력값
#1
#2
#3
#4
#5
#6

#이렇게도 되넴
for i in range(N):
    for j in range(M):
        print(arr[i][j])
        
