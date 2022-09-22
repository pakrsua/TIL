# 11659 구간 합 구하기 4
import sys

N, M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
accrue = [0]

for n in range(N):
    accrue.append(arr[n] + accrue[n])
# print(accrue)
for tc in range(M):
    x, y = map(int,sys.stdin.readline().split())
    print(accrue[y] - accrue[x - 1])