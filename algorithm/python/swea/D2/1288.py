# 1288. 새로운 불면증 치료법

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    ans = 0
    cnt_list = [0]*10
    cnt = 0
    while cnt != 10:
        ans += 1
        num_list = (str(num*ans))
        for i in num_list:
            if cnt_list[int(i)] == 0:
                cnt_list[int(i)] = 1
                cnt += 1

    print('#{} {}'.format(tc, num*(ans)))