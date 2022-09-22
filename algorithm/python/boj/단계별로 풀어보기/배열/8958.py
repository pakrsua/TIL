# OX퀴즈

T = int(input())

for tc in range(T):
    ox = list(input())
    cnt = 0
    score = 0
    for i in range(len(ox)):

        if ox[i] == 'O':
            cnt += 1
            score += 1*cnt
        else:
            cnt = 0

    print(score)