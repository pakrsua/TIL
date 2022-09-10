#10103 주사위 게임

N = int(input())
Aans = 100
Bans = 100
for tc in range(N):

    A, B = map(int, input().split())
    if A > B :
        Bans -= A
    elif B > A:
        Aans -= B

print(Aans)
print(Bans)