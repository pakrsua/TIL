# 1003 피보나치 함수
import sys

T = int(sys.stdin.readline())

for tc in range(T):
    N = int(sys.stdin.readline())
    zerocnt = [1, 0]
    onecnt = [0, 1]

    if N > 1:
        for i in range(N-1):
            zerocnt.append(onecnt[-1])
            onecnt.append(zerocnt[-2] + onecnt[-1])

    print(zerocnt)
    print(onecnt)
    print('{} {}'.format(zerocnt[N], onecnt[N]))