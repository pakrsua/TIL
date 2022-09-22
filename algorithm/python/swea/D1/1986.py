# 1986. 지그재그 숫자

T = int(input())

for tc in range(1, T + 1):
    num = int(input())

    ans = 0

    for i in range(1, num + 1):
        if i % 2:  # 홀수라면
            ans = ans + i
        else:  # 짝수라면
            ans = ans - i
    print('#{} {}'.format(tc, ans))