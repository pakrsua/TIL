# 퀵정렬

def QuickSort(a,left, right):
    if left < right:
        s = partition(a,left,right)
        print(s)
        QuickSort(a, left, s-1)
        QuickSort(a, s+1, right)


def partition(a, left, right):
    p = a[left]
    i = left
    j = right
    print(i, j)
    while i <= j:
        print(i, j)
        while i <= j and a[i] <= p:
            i += 1
        while i <= j and a[j] >= p:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[left], a[j] = a[j], a[left]
    return j

a = [5, 3, 1, 7, 9, 8, 6, 4, 2, 0]
QuickSort(a,0,len(a)-1)
print(a)