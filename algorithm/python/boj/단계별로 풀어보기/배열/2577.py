# 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

num = A * B * C
num = list(map(int,str(num)))

#카운팅 정렬 이용해보기
arr = [0] * 10

for i in range(len(num)):
    arr[num[i]] += 1
# print(arr) # 각 요소의 자리에 요소의 갯수를 더해준 값을 리스트화

# 한 줄에 하나씩 출력되도록
for i in arr:
    print(i)