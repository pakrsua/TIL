# 셀프 넘버

# 생성자 리스트
def self_num(d):
    if d < 10000:
        num = []
        for i in range(1, d+1):
            n = i
            n += int(str(i))
            n
            print(n)
    return True
for i in range(1,10001):
    print(self_num(i))