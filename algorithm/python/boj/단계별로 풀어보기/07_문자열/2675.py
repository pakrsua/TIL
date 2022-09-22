# 문자열 반복
T = int(input())

for tc in range(1, T+1):
    R, S = input().split()
    text = ''
    for i in S:
        for j in range(int(R)):
            text += i
    print(text)


# 틀림
# T = int(input())
#
# for tc in range(1, T+1):
#     R, S = input().split()
#
#     for i in S:
#         print(i*int(R),end='')