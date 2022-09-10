# 1764 듣보잡
import sys

N, M = map(int,sys.stdin.readline().split())
# 듣도 못한 사람
nohear = set()
# 보도 듣도 못한 사람
ans = set()

# 듣도 못한 사람을 받는다
for n in range(N):
    nohear.add(sys.stdin.readline().strip())
# 보도 못한 사람이 듣도 못한 리스트에 있는 경우 보도 듣도 못한 사람에 추가한다
for m in range(M):
    nolook = sys.stdin.readline().strip()
    if nolook in nohear:
        ans.add(nolook)
# 정렬
print(len(ans))
ans = sorted(list(ans))

# print(ans)
for i in ans:
    print(i)