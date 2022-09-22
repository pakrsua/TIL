# 10101 삼격형 외우기

A = int(input())
B = int(input())
C = int(input())

if A == 60 and B == 60 and C == 60:
    print('Equilateral')
elif A == B or B == C or A == C:
    if A + B + C == 180:
        print('Isosceles')
    else:
        print('Error')
else:
    if A + B + C == 180:
        print('Scalene')
    else:
        print('Error')