# 11721 열 개씩 끊어 출력하기

text = input()

for i in range(len(text)):
    if i % 10 == 9:
        print(text[i])
    else:
        print(text[i],end='')