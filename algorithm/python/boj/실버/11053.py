# 11053 가장 긴 증가하는 부분 수열
import sys

N = sys.stdin.readline().rstrip()
arr = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(0,i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

ans = max(dp)
print(ans)