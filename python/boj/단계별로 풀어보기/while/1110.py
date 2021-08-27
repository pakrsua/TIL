# 더하기 사이클

cnt = 0

new_num = int(input())
N = new_num

while True:
    if cnt > 0 and new_num == N:
        break
    else:
        second = new_num//10 + new_num % 10
        new_num = (new_num%10)*10 + (second%10)
        cnt += 1

print(cnt)