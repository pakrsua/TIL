# 9012 괄호

T = int(input())

for i in range(T):
    test = input()
    bracket = []
    flag ='YES'
    for t in test:
        if len(bracket) == 0:
            if t == ')':
                flag = 'NO'
                break
            elif t == '(':
                bracket.append(t)
        else:
            if t == '(':
                bracket.append(t)
            if t == ')' and bracket[-1] == '(':
                bracket.pop()
            elif t == ')' and bracket[-1] != '(':
                flag = 'NO'
                break
    if len(bracket) > 0:
        flag = 'NO'
    print(flag)