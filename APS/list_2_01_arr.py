##2차원 배열 받아오기##

N, M = map(int,input().split()) #행, 열 갯수 받기 *파이썬에서는 한 행씩 읽어와서 열에 대한 정보가 없어도 읽는데 문제가 없다
arr = [list(map(int, input().split())) for _ in range(N)]
# for _ in range() <- '_'큰 의미없이 단순 반복할 때 _넣으면 됨
print(arr)

#input 값
#2 3
#1 2 3
#4 5 6

#출력값
#[[1, 2, 3], [4, 5, 6]]


# 비어있는 배열 만들기
arr2 = [[0] * M for _ in range(N)]
#arr2 = [[0]*M]*N <- 모양은 만들어지지만 얉은 복사로 만들어지기 때문에 이렇게 만들면 x
arr3 = [[0]*M]*N

arr2[0][1] = 1
arr3[0][1] = 1

print(arr2)
print(arr3)

#출력값
#[[0, 1, 0], [0, 0, 0]]
#[[0, 1, 0], [0, 1, 0]]


# 1. 빈리스트 만들어 넣고 1차리스트 append하기

arr = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

# 2. 행의 공간을 미리 확보를 해두고 해당 자리를 바꾼다.
arr = [0] * N

for i in range(N):
    arr[i] = list(map(int,input().split()))

# 3. 리스트 내포 방식
# 위에거

