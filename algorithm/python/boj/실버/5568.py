# 5568 카드 놓기

def find(N):
    global cnt
    if len(card) == k:
        result = ""
        for i in card:
            result += str(i)
        if result not in ans:
            ans[result] = 1
            cnt += 1
        print(result)
    else:
        for i in range(N, k):
            card.append(arr[i])
            find(i)
            card.pop()

n = int(input())
k = int(input())
arr = []
card = []
ans = {}
cnt = 0
for t in range(n):
    arr.append(int(input()))
find(0)
print(cnt)