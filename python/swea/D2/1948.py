# 1948. 날짜 계산기
month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

T = int(input())

for tc in range(1, T+1):
    ans = 0
    fm, fd, sm, sd = map(int, input().split())
    if fm == sm:
        ans = sd - fd
    else:
        for i in range(fm, sm+1):
            if i == fm:
                ans += (month[i] - fd)
            elif i == sm:
                ans += sd
            else:
                ans += month[i]
    print('#{} {}'.format(tc, ans+1))