# 단어의 개수

text = input().strip()
# print(text)
cnt = 0
if len(text) == 0:
    print(0)
else:
    for i in text:
        if i == ' ':
            cnt += 1

    print(cnt+1)