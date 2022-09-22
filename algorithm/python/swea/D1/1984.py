# 1984. 중간 평균값 구하기

T = int(input())

for tc in range(1, T+1):
    num = list(map(int,input().split()))
    min_num = 10000
    max_num = 0

    for i in num:
        if min_num > i:
            min_num = i
        if max_num < i:
            max_num = i
    num.remove(min_num)
    # print(num)
    num.remove(max_num)
    # print(num)

    add = 0


    for i in num:
        add += i
    ans = add/len(num)

    print('#{} {:.0f}'.format(tc,ans))