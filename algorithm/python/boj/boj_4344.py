test_case = int(input())

for i in range(test_case):
    score = input().split()
    score = map(int, score)
    score = list(score)

    ans_cnt = 0
    
    add = 0
    avg = 0
    cnt = 0

    for score_avg in range(1, len(score)):
        add += score[score_avg]
        cnt += 1
        avg = add/cnt
        
    for upper_avg in range(1, len(score)):
        if avg < score[upper_avg]:
            ans_cnt += 1
        
    ans = ans_cnt / cnt * 100

    print(f'{ans:.3f}%')