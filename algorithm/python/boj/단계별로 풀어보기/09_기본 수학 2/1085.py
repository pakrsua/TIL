# 직사각형에서 탈출

x, y, w, h = map(int, input().split())

min =1000

if x < min:
    min = x
if y < min:
    min = y
if w - x < min:
    min = w-x
if h - y < min:
    min = h-y

print(min)