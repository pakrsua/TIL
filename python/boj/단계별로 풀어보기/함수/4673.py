# 셀프 넘버

# 생성자 리스트
def self_num(d):
    non_self_num = []
    num = 0

    for i in str(d):
        num += d
        num += int(i)
        if not num in non_self_num:
            non_self_num.append(num)
    print(non_self_num)
    return True

for i in range(1,10001):
    print(self_num(i))