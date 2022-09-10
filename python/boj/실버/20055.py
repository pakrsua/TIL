# 20055 컨베이어 벨트 위의 로봇

N, K = map(int,input().split())
A = list(map(int,input().split()))
robot = [0] * (N*2)
ans = 1
zero_cnt = 0

while True:
    # if A[0] != 0 and A[N-1] != 0:
    #     A[0] -= 1
    #     A[N-1] -= 1
    # else:
    #     zero_cnt = 0
    #     for i in range(N):
    #         if A[i] == 0:
    #             zero_cnt += 1
    # print(zero_cnt)
    # if zero_cnt >= K:
    #     break
    # print(A)
    # A.append(A[0])
    # A.pop(A[0])
    #
    # ans += 1


    # for i in range(N):
    #     if A[i] == 0:
    #         zero_cnt += 1
    # if zero_cnt >= K:
    #     break
    #
    # A.append(A[0])
    # A.pop(0)
    #
    # A[0] -= 1
    # A[N-1] -= 1
    #
    # ans += 1


    robot[0] += 1
    for i in range(N):
        if A[i] == 0:
            zero_cnt += 1

    if zero_cnt >= K:
        break

    A.insert(0, A[(N*2)-1])
    A.pop()
    robot.insert(0, robot[(N*2)-1])
    robot.pop()
    print(A)
    if robot[0] == 1:
        A[0] -= 1
    if robot[N-1] == 1:
        A[N-1] -= 1

    ans += 1

print(ans)

