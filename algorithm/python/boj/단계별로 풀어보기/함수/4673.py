# 셀프 넘버

# 생성자 리스트
def self_num(d):
    global non_self_num
    num = 1
    for i in str(d):
        num += d
        num += int(i)
        if not num in non_self_num:
            if num < 10000:
                non_self_num.append(num)

    return

non_self_num = []
for i in range(1,10001):
    self_num(i)
ans = set(non_self_num)

for i in range(len(ans)):
    print(i)