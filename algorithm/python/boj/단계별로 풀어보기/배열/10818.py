# 10818 최소, 최대

# N = int(input())
# num = list(map(int, input().split()))
#
# for i in range(N-1, -1, -1):
#     for j in range(0, i):
#         if num[j] > num[j+1]:
#             num[j], num[j+1] = num[j+1], num[j]
#
# print('{} {}'.format(num[0],num[-1]))

N = int(input())
num = list(map(int, input().split()))

print('{} {}'.format(min(num), max(num)))