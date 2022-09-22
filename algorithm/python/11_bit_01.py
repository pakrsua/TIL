# 비트 연산 예제1

def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        if i & (1 << j):
            output += '1'
            print('{} {}'.format(i,output))
        else:
            output += '0'
    print(output)

for i in range(-5, 6):
    print('%3d = '%i, end='')
    Bbit_print(i)