def unionConnect(a, b):
    global arr
    if a < b:
        arr[b] = a
    else:
        arr[a] = b

def getParentNode(x):
    global arr
    if arr[x] == x:
        return x
    return getParentNode(arr[x])

def findParentNode(a, b):
    a = getParentNode(a)
    b = getParentNode(b)
    if (a == b):
        print(1)
    else:
        print(0)


arr = [0] * 11
for i in range(1,11):
    arr[i] = i
    unionConnect(1, 2)
    unionConnect(2, 3)
    unionConnect(3, 4)
    unionConnect(5, 6)
    unionConnect(6, 7)
    unionConnect(7, 8)
findParentNode(2,4)
print(arr)