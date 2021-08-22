# 이진탐색

def binarySearch(a, key):
    start = 0
    end = len(a)-1

    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15]

print(binarySearch(arr, 4))
print(binarySearch(arr,12))