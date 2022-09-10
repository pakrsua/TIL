# 11650 좌표 정렬하기
import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    x, y = map(int,sys.stdin.readline().split())
    arr.append([x,y])

arr.sort()

for i in range(n):
    print(*arr[i])