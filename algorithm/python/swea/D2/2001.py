T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    fly = [list(map(int, input().split())) for _ in range(N)]
    attack = [[0] * M for __ in range(M)]
    max_num = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            add_num = 0
            for fly_i in range(M):
                for fly_j in range(M):
                    add_num += fly[i + fly_i][j + fly_j]
                    if add_num > max_num:
                        # print(add_num)
                        max_num = add_num

    print('#{} {}'.format(tc, max_num))