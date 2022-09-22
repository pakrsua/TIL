# 1181 단어 정렬
import sys

N = int(sys.stdin.readline())
text = []

for i in range(N):
    text.append(sys.stdin.readline().strip())

set_text = set(text)
text = list(set_text)

text.sort()
text.sort(key=len)
for i in range(len(text)):
    print(text[i])

# 아래 코드는 시간 초과 난 코드 또륵 하나하나 비교했다
# for i in range(len(text)):
#     for j in range(i,len(text)):
#         if len(text[i]) > len(text[j]):
#             text[i],text[j] = text[j],text[i]
# # print(text)
# for i in range(len(text)):
#     for j in range(i,len(text)):
#         if text[i] > text[j] and len(text[i]) == len(text[j]):
#             text[i],text[j] = text[j], text[i]