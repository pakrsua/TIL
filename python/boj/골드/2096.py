# 2096 내려가기

N = int(input())

arr = list(map(int, input().split()))
max_list = arr
min_list = arr

for t in range(N-1):
    a, b, c = map(int, input().split())
    max_list = [a + max(max_list[0],max_list[1]), b + max(max_list), c + max(max_list[1],max_list[2])]
    min_list = [a + min(min_list[0],min_list[1]), b + min(min_list), c + min(min_list[1],min_list[2])]
print(max(max_list))
print(min(min_list))