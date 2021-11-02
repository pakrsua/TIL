# 11445. 무한사전

T = int(input())

for tc in range(1, T+1):
    P = input().strip()
    Q = input().strip()

    ans = 'Y'
    NewP = P+'a'
    if NewP == Q:
      ans = 'N'

    print('#{} {}'.format(tc, ans))