# 25193 곰곰이의 식단 관리

N = int(input())
food = input()
c = 0
another = 0
ans = 0
for t in range(N):
    if food[t] == 'C':
        c += 1
    else:
        another += 1
if another == 0:
    ans = c
else:
    ans = c // (another + 1)

    if c % (another+1) != 0:
        ans += 1
print(ans)