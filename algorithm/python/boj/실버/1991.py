# 1991 트리 순회
def preorder(n):
    print(arr[n][0],end='')
    if arr[n][1] != '.':
        for i in range(len(arr)):
            if arr[i][0] == arr[n][1]:
                preorder(i)
    if arr[n][2] != '.':
        for i in range(len(arr)):
            if arr[i][0] == arr[n][2]:
                preorder(i)
def inorder(n):
    if arr[n][1] != '.':
        for i in range(len(arr)):
            if arr[i][0] == arr[n][1]:
                inorder(i)
    print(arr[n][0],end='')
    if arr[n][2] != '.':
        for i in range(len(arr)):
            if(arr[i][0]) == arr[n][2]:
                inorder(i)
def postorder(n):
    if arr[n][1] != '.':
        for i in range(len(arr)):
            if arr[i][0] == arr[n][1]:
                postorder(i)
    if arr[n][2] != '.':
        for i in range(len(arr)):
            if(arr[i][0]) == arr[n][2]:
                postorder(i)
    print(arr[n][0],end='')

N = int(input())
arr = []

for t in range(N):
    arr.append(list(map(str,input().split())))

preorder(0)
print()
inorder(0)
print()
postorder(0)