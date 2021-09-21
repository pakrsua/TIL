# 1983. 조교의 성적 매기기
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    score_list = []
    sort_list = []
    for i in range(N):
        m_test, f_test, hw = map(int, input().split())
        score = (0.35*m_test + 0.45*f_test + 0.2*hw)
        score_list.append(score)
        sort_list.append(score)


    # score_list 정렬
    for i in range(N):
        for j in range(i,N):
            if sort_list[i] < sort_list[j]:
                sort_list[i],sort_list[j] = sort_list[j], sort_list[i]

    for i in range(N):
        if sort_list[i] == score_list[K-1]:
            grade_idx = i//(N//10)

            print('#{} {}'.format(tc, grade[grade_idx]))