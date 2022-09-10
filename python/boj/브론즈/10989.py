# 10989 수 정렬하기 3
import sys
N = int(sys.stdin.readline())
nums = [0] * 10001
for t in range(N):
    nums[int(sys.stdin.readline())] += 1
for i in range(10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)