# 상수
num1, num2 = input().split()
sangsu1 = num1[::-1]
sangsu2 = num2[::-1]

if sangsu1>sangsu2:
    print(sangsu1)
else:
    print(sangsu2)