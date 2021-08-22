#   ** bubble sort**

##01## 따라해보기
def BubbleSort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a

def BubbleSort_2(arr):
    for i in range(len(arr)-1):
        for j in range(i, len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# my_list = [1,5,7,9,5,4,3,6,1,10]
# print(BubbleSort(my_list))

my_list = [1, 3, 5, 7, 9, 8, 4, 6, 2, 10]
print(BubbleSort_2(my_list))

##직접 짜보기## ----------------------------------이렇게 순서를 앞에서부터 짜면 안정정렬이 아니게 되는건가....?
#-------> 안정정렬과 상관없이 일단 버블 정렬은 인접값을 계산하는 것이기 때문에 이 코드는 버블 정렬이 아니다.
# def BubbleSort(a):
#     for i in range(len(a)):
#         for j in range(i , len(a)):
#             if a[i] > a[j]:
#                 a[i],a[j] = a[j],a[i]
#     return a

# my_list = [1,5,7,9,5,4,3,6,1,10]
# print(BubbleSort(my_list))
#-> 버블정렬 아님

