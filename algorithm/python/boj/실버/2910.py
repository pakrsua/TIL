# 2910 빈도 정렬

N, C = map(int,input().split())
arr = {}
text = list(map(int,input().split()))
for i in text:
    if i in arr:
        arr[i] += 1
    else:
        arr[i] = 1
ans = sorted(arr.items(),key=lambda x:-x[1])
for i in range(len(ans)):
    for j in range(ans[i][1]):
        print(ans[i][0],end=' ')