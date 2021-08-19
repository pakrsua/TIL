# 알람 시계

h, m = map(int,input().split())

if m < 45 :
    m = m + (60 - 45)
    if h != 0:
        h -= 1
    else:
        h = 23
else:
    m = m - 45

print('{} {}'.format(h, m))