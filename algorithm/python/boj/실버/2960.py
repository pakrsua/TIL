# 2960 에라노스테네스의 체

N, K = map(int,input().split())
arr = []
cnt = 0
ans = 0

for i in range(2, N+1):
    arr.append(i)

min_num = arr[0]

while cnt < K:
    i = 1
    while min_num * i < N + 1:
        if min_num * i in arr:
            cnt += 1
            arr.remove(min_num * i)
            if cnt == K:
                ans = min_num * i
        i += 1
        # print(arr)
    if len(arr) > 0:
        min_num = arr[0]
print(ans)