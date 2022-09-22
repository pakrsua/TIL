# 2562 최댓값

arr = []
max_num = 0
idx = 0

for tc in range(9):
    arr += [int(input())]

for i in range(len(arr)):
    if arr[i] > max_num:
        max_num = arr[i]
        idx = i
print(max_num)
print(idx+1)