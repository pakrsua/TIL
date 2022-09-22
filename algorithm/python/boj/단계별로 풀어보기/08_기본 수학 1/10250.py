# 10250. ACM 호텔

T = int(input())
for tc in range(T):
    H, W, N = map(int, input().split())

    hotel = [[0]*W for _ in range(H)]
    ans = 0

    for j in range(W):
        for i in range(H-1, -1, -1):
            if N == 1:
                if j < 9:
                    print('{}0'.format(H-i), end='')
                else:
                    print('{}'.format(H-i), end='')
                print(j+1)
            if N > 0:
                hotel[i][j] = N
                N -= 1


    # print(hotel)
