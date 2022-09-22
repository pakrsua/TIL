# 4949 균형잡힌 세상
while True:
    t = input()
    bracket = []
    flag = 'yes'
    if t == '.':
        break
    for i in range(len(t)):
        if len(bracket) == 0:
            if t[i] == ')' or t[i] ==']':
                flag = 'no'
                break
            elif t[i] == '(' or t[i] == '[':
                bracket.append(t[i])
        else:
            if t[i] == '(':
                bracket.append(t[i])
            if t[i] == '[':
                bracket.append(t[i])
            if t[i] == ')' and bracket[-1] == '(':
                bracket.pop()
            elif t[i] == ')' and bracket[-1] != '(':
                flag = 'no'
                break
            elif t[i] == ']' and bracket[-1] == '[':
                bracket.pop()
            elif t[i] == ']' and bracket[-1] != '[':
                flag= 'no'
                break
    if len(bracket) != 0:
        flag = 'no'
    print(flag)