# 크로아티아 알파벳

cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']

text = input()

for i in cro:
    if i in text:
        text = text.replace(i,'a')

# print(text)
print(len(text))