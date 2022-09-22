# 그룹 단어 체커

T = int(input())
cnt = 0

for tc in range(T):
    text = input()
    flag = 'T'

    for i in range(len(text)):
        if i < len(text)-2:
            if text[i] != text[i+1]:
                for j in range(i+1,len(text)):
                    if text[i] == text[j]:
                        flag = 'F'
    if flag == 'T':
        cnt += 1

print(cnt)