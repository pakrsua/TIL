# 11723 집합
import sys

S = set([])
M = int(sys.stdin.readline())

for tc in range(M):
    oper = sys.stdin.readline().split()

    if len(oper) <= 1:
        if oper[0] == 'all':
            S = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])
        elif oper[0] == 'empty':
            S = set([])
    else:
        if oper[0] == 'add':
            S.add(oper[1])
        elif oper[0] == 'remove':
            if oper[1] in S:
                S.remove(oper[1])
        elif oper[0] == 'check':
            if oper[1] in S:
                print(1)
            else:
                print(0)
        elif oper[0] == 'toggle':
            if oper[1] in S:
                S.remove(oper[1])
            else:
                S.add(oper[1])
    # print(S)