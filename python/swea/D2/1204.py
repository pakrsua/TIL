# [s/w 문제해결 기본] 1일차 - 최빈수 구하기

T = int(input())

for tc in range(1, T+1):
    test_case = int(input())
    score_list = list(map(int,input().split()))
    max_num = 0
    max_idx = 0

    counts = [0] * 101

    for i in range(1000):
        counts[score_list[i]] += 1
    # print(counts)

    for i in range(101):
        if counts[i] >= max_num:
            max_num = counts[i]
            max_idx = i
    print('#{} {}'.format(tc, max_idx))