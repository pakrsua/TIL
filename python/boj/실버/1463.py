# 1463 1로 만들기

# X = int(input())
# cnt = 0
#
# while X != 1:
#     if X % 3 == 0:
#         X = X // 3
#         cnt += 1
#     if X % 2 == 0:
#         X = X // 2
#         cnt += 1
#     else:
#         X -= 1
#         cnt += 1
#     print(X)
# print(cnt)

x = int(input())
arr = [0] * (x + 1)

for i in range(2, x+1):
    arr[i] = arr[i - 1] + 1

    if i % 3 == 0:
        arr[i] = min(arr[i],arr[i//3] + 1)
    if i % 2 == 0:
        arr[i] = min(arr[i],arr[i//2] + 1)

    print(arr)
print(arr[x])