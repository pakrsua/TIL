# 한수
def hansu(n):
    X = 0

    for i in range(1, n+1):
        if i < 100:
            X += 1
        else:
            hansus = list(map(int,str(i)))
            # print(hansus)
            if hansus[0] - hansus[1] == hansus[1] - hansus[2]:
                X += 1
    return X


N = int(input())
print(hansu(N))