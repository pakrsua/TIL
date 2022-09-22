# 2839. 설탕 배달

N = int(input())
cnt = 0

while N > 0:
    if N % 5 == 0:
        N -= 5
        cnt += 1
        N
        print('남은 설탕 수 : {} 봉지 수 :{}'.format(N,cnt))
    elif N % 3 == 0:
        N -= 3
        cnt += 1
        print('남은 설탕 수 : {} 봉지 수 :{}'.format(N,cnt))
    elif N > 5:
        N -= 5
        cnt += 1
        print('남은 설탕 수 : {} 봉지 수 :{}'.format(N,cnt))
    elif N == 3:
        cnt += 1
        print('남은 설탕 수 : {} 봉지 수 :{}'.format(N,cnt))
        break
    else:
        cnt = -1
        print('남은 설탕 수 : {} 봉지 수 :{}'.format(N,cnt))
        break
print(cnt)