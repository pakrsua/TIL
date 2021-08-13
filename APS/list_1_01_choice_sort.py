## 선택정렬
## 1. 리스트의 최소값을 찾는다
## 2. 찾은 최소값을 맨 앞에 있는 값과 교체한다
## 3. 리스트를 순회하며 1, 2번을 반복한다(뒤의 값이 더 작을 경우 해당 값의 인덱스와 현재 가지고 있는 인덱스 변호를 교환)


#######################################################
def selectionSort(num):
    N = len(num)
    for i in range(N-1):
        idx_min = i
        for j in range(i+1,N):
            if num[idx_min] > num[j]:
                idx_min = j
        num[i], num[idx_min] = num[idx_min], num[i]

    return num

my_list = list(map(int,input().split()))
print(selectionSort((my_list)))
###########################################################