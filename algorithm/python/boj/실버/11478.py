# 11478 서로 다른 부분 문자열의 개수

S = input()
s_arr = set()

for i in range(len(S)):
    text = ''
    for j in range(i,len(S)):
        text += S[j]
        s_arr.add(text)
print(len(s_arr))