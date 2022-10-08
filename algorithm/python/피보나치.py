n = int(input())

# 반복문으로 풀기
arr = [0, 1, 1]

for i in range(3, 101):
    arr.append(arr[i - 1] + arr[i - 2])
print('반복문:{}'.format(arr[n]))

# 재귀로 풀기
# 메모리제이션
arr_2 = [0]*(n+1)
def recursive(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    if arr_2[x] == 0:
        arr_2[x] = recursive(x-1) + recursive(x - 2)
    return arr_2[x]

print('재귀:{}'.format(recursive(n)))