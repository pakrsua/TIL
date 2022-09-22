# 5430 AC
import sys

T = int(sys.stdin.readline())

for tc in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    arr = sys.stdin.readline()[1:-2].split(',')
    flag = 1
    rCnt = 0

    if n == 0:
        arr = []

    for pc in range(len(p)):
        if p[pc] == "R":
            rCnt += 1

        if p[pc] == "D":
            if len(arr) == 0:
                flag = -1
                break
            if rCnt % 2 != 0:
                arr.pop()
            else:
                arr.pop(0)
        if pc == len(p)-1:
            if rCnt % 2 != 0:
                arr.reverse()

    # print(arr)
    if flag == -1:
        print("error")
    else:
        print("[",end='')
        print(','.join(arr),end='')
        print("]")