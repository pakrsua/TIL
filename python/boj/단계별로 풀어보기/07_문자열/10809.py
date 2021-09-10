# 알파벳 찾기

S = input()

for i in range(97, 123):
    char = chr(i)
    if char in S:
        print(S.index(char))
    else:
        print(-1)