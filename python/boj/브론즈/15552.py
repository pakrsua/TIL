#15552 빠른 A+B
import sys

T = int(input())

for tc in range(T):
    A, B = map(int,sys.stdin.readline().split())
    print(A+B)