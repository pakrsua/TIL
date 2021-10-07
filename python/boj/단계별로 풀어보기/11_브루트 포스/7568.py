# 7568. 덩치

# T = int(input())
#
# dungchi = [list(map(int,input().split())) for _ in range(T)]
# for i in range(1, T+1):
#     dungchi[i-1].append(i)
# dungchi.sort(key=lambda x:x[0], reverse=True)
#
# print(dungchi)
#
# rank = 1
# idx = 0
# while idx < T-1:
#     add = 0
#     for j in range(idx+1,T):
#         if dungchi[idx][1] < dungchi[j][1]:
#             add += 1
#             break
#     dungchi[idx].append(rank)
#     rank += add
#     idx += 1
# print(dungchi)

# T = int(input())
# people = [list(map(int,input().split())) for _ in range(T)]
#
# cnt_list = []
#
# for i in range(T):
#     cnt = 1
#     for j in range(T):
#         if people[i][0] < people[j][0] or people[i][1] < people[j][1]:
#             cnt += 1
#         elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
#             cnt += 1
#
#     cnt_list.append(cnt)
# print(cnt_list)

T = int(input())
people = [list(map(int,input().split())) for _ in range(T)]

cnt_list = []

for i in range(T):
    cnt = 1
    for j in range(T):
        if people[i][0] < people[j][0] or people[i][1] < people[j][1]:

            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                cnt += 1

    cnt_list.append(cnt)

for i in cnt_list:
    print(i,end=' ')