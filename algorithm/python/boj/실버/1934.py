#1934 최소 공배수
import sys

T = int(input())

for tc in range(T):
    A, B = map(int, sys.stdin.readline().split())
    a = A
    b = B
    while True:
        r = a % b
        if r == 0:
            break
        a = b
        b = r
    # 최소공배수 = b
    print((A//b)*(B//b)*b)