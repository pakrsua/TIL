#3058

T = int(input())

for tc in range(T):
    num = list(map(int,input().split()))
    even = []
    add = 0


    for n in range(7):
        if num[n] % 2 == 0:
            even.append(num[n])
            add += num[n]
    print('{} {}'.format(add,min(even)))