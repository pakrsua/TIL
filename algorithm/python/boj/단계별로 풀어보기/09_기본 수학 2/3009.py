# 네 번째 점

dotx_1, doty_1 = map(int,input().split())
dotx_2, doty_2 = map(int,input().split())
dotx_3, doty_3 = map(int,input().split())

x = [dotx_1, dotx_2, dotx_3]
y = [doty_1, doty_2, doty_3]

for i in range(3):
    if x.count(x[i]) == 1:
        print(x[i], end =' ')
for i in range(3):
    if y.count(y[i]) == 1:
        print(y[i])