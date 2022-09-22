# 10886

N= int(input())
cute=0
notcute=0

for tc in range(N):
    if int(input()) == 1:
        cute += 1
    else:
        notcute += 1
if cute > notcute:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')