# 나머지

arr = []

for tc in range(10):
    arr += [int(input())]

arr_2 = []

for i in arr:
    arr_2.append(i%42)

arr_3 = []

for i in arr_2:
    if not i in arr_3:
        arr_3.append(i)

print(len(arr_3))