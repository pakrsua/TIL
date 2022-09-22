# 백만 장자 프로젝트

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int,input().split()))

    max_num = 0
    ans_price = 0

    for i in range(N-1,-1,-1):
        if price[i] > max_num:
            max_num = price[i]
        else:
            ans_price += max_num - price[i]

    print('#{} {}'.format(tc, ans_price))