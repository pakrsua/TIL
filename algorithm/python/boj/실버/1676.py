# 1676 팩토리얼 0의 개수

N = int(input())
num = 1
cnt = 0

for i in range(1, N+1):
    num *= i
# print(num)
for i in range(len(str(num))-1,-1,-1):
    if str(num)[i] == "0":
        cnt += 1
    else:
        break

print(cnt)