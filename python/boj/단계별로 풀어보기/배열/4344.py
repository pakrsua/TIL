# 평균은 넘겠지

C = int(input())

for tc in range(C):
    score = list(map(int, input().split()))
    over_avg = 0

    avg = sum(score[1:])/score[0]

    for i in score[1:]:
        if i > avg:
            over_avg += 1

    ans = over_avg/score[0] * 100

    print('{:.3f}%'.format(ans))