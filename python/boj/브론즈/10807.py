# 10807 개수 세기

N = int(input())
arr =list(map(int,input().split()))
cnt = 0
v = int(input())
for i in arr:
    if v == i:
        cnt +=1
print(cnt)