# 10039
hap = 0
for t in range(5):
    num = int(input())
    if num > 40:
        hap += num
    else:
        hap += 40
print(hap//5)