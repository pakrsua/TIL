# 직각삼각형

while True:
    num = list(map(int,input().split()))
    if sum(num) == 0:
        break
    max_num = max(num)

    add = 0

    for i in range(3):
        if num[i] != max_num:
            add += num[i]*num[i]


    if max_num*max_num == add:
        print('right')
    else:
        print('wrong')