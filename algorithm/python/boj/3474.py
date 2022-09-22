# 3474 교수가 된 현우

# T = int(input())
#
# for tc in range(1, T+1):
#     num = int(input())
#     fac_num = 1
#     zero_cnt = 0
#
#     for i in range(num):
#         fac_num *= num-i
#     # print(fac_num)
#     fac_num = str(fac_num)
#     # print(len(fac_num))
#     for i in range(len(fac_num)-1, -1, -1):
#         if fac_num[i] == '0':
#             zero_cnt += 1
#         else:
#             break
#     print(zero_cnt)

# T = int(input())
#
# for tc in range(1, T+1):
#     num = int(input())
#     ans = 0
#
#     for i in range(1, num+1):
#         five = 5
#         if i % five == 0:
#             ans += 1
#             while five < num:
#                 five *= 5
#                 if i % five == 0:
#                     ans += 1
#     print(ans)

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    ans = 0

    while num >= 5:
        ans += num // 5
        num //= 5
    print(ans)