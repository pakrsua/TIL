# 1620 나는야 포켓몬 마스터 이다솜
import sys

N, M = map(int,sys.stdin.readline().split())
pocketmon = []

for n in range(N):
    pocketmon.append(sys.stdin.readline())

print(pocketmon)

for m in range(M):
    mon = sys.stdin.readline().strip()
    if mon.isdigit():
        print(pocketmon[int(mon) - 1])
    else:
        print(pocketmon.index(mon) + 1)