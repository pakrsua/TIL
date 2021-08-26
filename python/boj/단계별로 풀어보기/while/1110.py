# 더하기 사이클

cnt = 0

# if N < 10:
#     print(N*11)
#
# print(((N&10)*10) + ((N%10)+(N//10))%10)
new_num = int(input())
N = new_num

while True:
    if cnt > 0 and new_num == N:
        break
    else:
        second = new_num//10 + new_num % 10
        new_num = (new_num%10)*10 + (second%10)
        # print(new_num)
        cnt += 1

print(cnt)