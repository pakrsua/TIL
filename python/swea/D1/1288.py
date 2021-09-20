# 1288. 새로운 불면증 치료법

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    ans = 0
    num_list = []

    while True:
        ans += 1
        num_list.extend(str(num*ans))
        set_list = set(num_list)
        set_list = list(set_list)
        print(set_list)
        print(num_list)


    print('#{} {}'.format(tc, ans))