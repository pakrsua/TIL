# 평균

# N = int(input())
# score = list(map(int, input().split()))
# max_num = 0
# new_score = []
#
# for i in range(N):
#     if score[i] > max_num:
#         max_num = score[i]
# for i in score:
#     new_score.append(i/max_num*100)
#
# # 평균 구하기
# add = 0
#
# for i in new_score:
#     add += i
#
# print(add/N)

N = int(input())
score = list(map(int, input().split()))
max_num = 0
new_score = []

for i in range(N):
    if score[i] > max_num:
        max_num = score[i]
for i in score:
    new_score.append(i/max_num*100)

print(sum(new_score)/N)