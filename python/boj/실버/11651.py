# 11651 좌표 정렬하기 2
import sys

N = int(sys.stdin.readline())
arr = []

for tc in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))
arr.sort(key=lambda x:(x[0]))
arr.sort(key=lambda x:(x[1]))
for i in range(N):
    print(*arr[i])