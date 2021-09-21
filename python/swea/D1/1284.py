# 수도 요금 경쟁

T = int(input())

for tc in range(1, T+1):
    p, q, r, s, w = map(int, input().split())

    Asudo = p*w

    Bsudo = 0

    if w < r:
        Bsudo = q
    else:
        Bsudo = q + (w-r)*s

    if Asudo < Bsudo:
        print('#{} {}'.format(tc, Asudo))
    else:
        print('#{} {}'.format(tc, Bsudo))