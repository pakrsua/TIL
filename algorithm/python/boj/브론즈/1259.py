# 1259 팰린드롬수

while(1):
    num = input()
    if num == '0':
        break
    mun = num[::-1]
    if mun == num:
        print('yes')
    else:
        print('no')