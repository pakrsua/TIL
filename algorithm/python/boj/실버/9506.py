# 9506 약수들의 합

# 숫자를 계속 입력받기
while True:
    n = int(input())
    # -1을 받으면 while문 종료
    if n == -1:
        break

    ans = []
    add = 0
    # 나누어지면 약수로 배열에 넣어주기
    # 자동 오름차순
    for i in range(1, n):
        if n % i == 0:
            ans.append(i)

    for i in range(len(ans)):
        add += ans[i]

    if add != n:
        print('{} is NOT perfect.'.format(n))
    else:
        print('{} ='.format(n),end=' ')
        for i in range(len(ans)):
            # 마지막 숫자의 뒤에는 + 를 빼주기
            if i == len(ans)-1:
                print('{}'.format(ans[i]))
            else:
                print('{} +'.format(ans[i]), end=' ')