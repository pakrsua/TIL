# 11387. 몬스터 사냥

T = int(input())

for tc in range(1, T+1):
    d,l,n = map(int,input().split())

    damage = 0

    for i in range(n):
        damage += d * (1+(i*l*0.01))

    print('#{} {}'.format(tc, int(damage)))