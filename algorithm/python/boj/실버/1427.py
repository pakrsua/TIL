# 1427 소트인사이드

num = list(input())

for i in range(len(num)):
    for j in range(i,len(num)):
        if num[i] < num[j]:
            num[i], num[j] = num[j], num[i]

# print(*num)
for i in range(len(num)):
    print(num[i],end='')