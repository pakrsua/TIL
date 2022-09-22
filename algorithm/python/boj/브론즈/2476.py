# 2476. 주사위 게임

N = int(input())

max_ans = 0

for tc in range(N):
    cube = list(map(int,input().split()))
    ans = 0
    max_cnt = 0
    max_num = 0

    for i in range(3):
        cnt = 0
        for j in range(3):
            if cube[i] == cube[j]:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            max_num = cube[i]
    if max_cnt == 1:
        max_num = max(cube)

    if max_cnt == 3:
        ans = 10000 + max_num * 1000
    elif max_cnt == 2:
        ans = 1000 + max_num * 100
    else:
        ans = max_num * 100

    if ans > max_ans:
        max_ans = ans
print(max_ans)