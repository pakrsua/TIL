# 14490 백대열

n, m = map(int,input().split(':'))
a, b = n, m
if n > m:
    while m > 0:
        n, m = m, n % m
    print(a // n, end='')
    print(':', end='')
    print(b // n)
else:
    while n > 0:
        n, m = m % n, n
    print(a//m,end='')
    print(':',end='')
    print(b//m)
