# 1920 수 찾기
import sys

def binery(i, start, end):
    if start > end:
        return 0
    middle = (start+end)//2
    if i == nArr[middle]:
        return 1

    elif(i < nArr[middle]):
         return binery(i, start, middle - 1)
    else:
        return binery(i, middle + 1, end)


N = int(input())
nArr = list(map(int,sys.stdin.readline().split()))
nArr.sort()

M = int(input())
mArr = list(map(int,sys.stdin.readline().split()))

for i in mArr:
    print(binery(i,0,N-1))