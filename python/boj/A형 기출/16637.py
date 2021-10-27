# 괄호 추가하기

N = int(input())
num = input()

max_add = 0
add = 0

q = []

for i in range(N):
    q.append(num[i])

# q에 있는거 계산하는 식

while len(q) > 1:
    if q[1] == '+':
        q.insert(0,int(q[0]) + int(q[2]))
        q.pop(1)
        q.pop(1)
        q.pop(1)
    if q[1] == '-':
        q.insert(0, int(q[0]) - int(q[2]))
        q.pop(1)
        q.pop(1)
        q.pop(1)
    if q[1] == '*':
        q.insert(0, int(q[0]) * int(q[2]))
        q.pop(1)
        q.pop(1)
        q.pop(1)
print(q)