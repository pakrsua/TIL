# 손익 분기점

# A 고정비 B 생산비 C 가격

a, b, c = map(int, input().split())

if b >= c:
    print(-1)

else : print((a//(c-b))+1)