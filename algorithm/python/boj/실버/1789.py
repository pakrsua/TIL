# 1789 수들의 합

S = int(input())
num = 1
ans = 0

while ans <= S:
    ans += num
    if ans >= S-num:
        break
    # print('num : {}, ans : {}'.format(num,ans))
    num += 1
print(num)