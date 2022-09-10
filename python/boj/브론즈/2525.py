# 2525 오븐 시계

hour, min = map(int,input().split())
C = int(input())

min += C % 60

hour += C // 60

if min == 60:
    min = 0
    hour += 1
if min >= 60:
    min -= 60
    hour += 1
if hour >= 24:
    hour -= 24

print('{} {}'.format(hour, min))