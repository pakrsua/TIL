# 2056. 연월일 달력

T = int(input())

for tc in range(1, T+1):
    date = input()
    flag = 0

    year = date[0:4]
    month = date[4:6]
    day = date[6:8]

    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) > 31:
            flag = -1
    elif int(month) in [4, 6, 9, 11]:
        if int(day) > 30:
            flag = -1
    elif int(month) == 2:
        if int(day) > 28:
            flag = -1
    else:
        flag = -1

    if flag == -1:
        print('#{} -1'.format(tc))

    else:
        print('#{} {}/{}/{}'.format(tc, year, month, day))