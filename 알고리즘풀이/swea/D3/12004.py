# 12004. 구구단1

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    ans = 'No'

    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == num:
                ans = 'Yes'

    print('#{} {}'.format(tc, ans))