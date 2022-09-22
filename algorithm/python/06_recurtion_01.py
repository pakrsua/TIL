# 재귀함수 연습 01 팩토리얼 계산해보기

# 재귀함수를 이용한 팩토리얼 계산 함수
def fac (num):
    gap = num
    if num <= 1:
        return gap
    else:
        gap = gap * fac(num-1)
        return gap

# 반복문으로 팩토리얼 계산
def fac_for (num):
    gap = 1
    for i in range(num):
        gap += gap * i
    return gap

factorial = int(input())

print(fac(factorial))
print(fac_for(factorial))