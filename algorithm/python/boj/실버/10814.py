# 10814 나이순 정렬

N = int(input())
people = []

for t in range(N):
    age, name = input().split()
    people.append([int(age),name])
# 숫자만 기준으로 정렬
people.sort(key = lambda people:people[0])

for i in range(N):
    print('{} {}'.format(people[i][0],people[i][1]))