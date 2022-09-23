#9372 상근이의 여행
import sys

T = int(input())

for tc in range(T):
    N, M = map(int,sys.stdin.readline().rstrip().split())
    arr = [[] * (N+1) for _ in range(N+1)]
    for i in range(M):
        a,b = map(int,sys.stdin.readline().rstrip().split())
    print(N-1)