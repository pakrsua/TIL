#   ** bubble sort**

##01## 따라해보기
# def BubbleSort(a):
#     for i in range(len(a)-1, 0, -1):
#         for j in range(0, i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]

#     return a

# my_list = [1,5,7,9,5,4,3,6,1,10]
# print(BubbleSort(my_list))

##직접 짜보기## ----------------------------------이렇게 순서를 앞에서부터 짜면 안정정렬이 아니게 되는건가....?
def BubbleSort(a):
    for i in range(len(a)):
        for j in range(i , len(a)):
            if a[i] > a[j]:
                a[i],a[j] = a[j],a[i]
    return a

my_list = [1,5,7,9,5,4,3,6,1,10]
print(BubbleSort(my_list))