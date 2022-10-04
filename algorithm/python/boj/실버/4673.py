# 4673 셀프 넘버

arr = []
for i in range(1,10001):
    arr.append(i)

for i in range(1, 10001):
    nums=list(str(i))
    num = i
    for j in range(len(nums)):
        num += int(nums[j])
    if num in arr:
        arr.remove(num)

for i in arr:
    print(i)