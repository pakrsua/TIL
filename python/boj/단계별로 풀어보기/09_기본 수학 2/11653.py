# 소인수분해

N = int(input())
num = N
factorizaton = []
i = 2
while num > 1:
    if num % i == 0:
        num = num//i
        factorizaton.append(i)
        continue
    i += 1

for i in factorizaton:
    print(i)