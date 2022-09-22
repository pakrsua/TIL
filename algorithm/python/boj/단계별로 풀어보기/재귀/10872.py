# 10872 팩토리얼
def factorial(num):
    ans = num
    if num == 0:
        return 1
    elif num <= 1:
        return ans
    else:
        ans = ans * factorial(num-1)
        return ans

N = int(input())
print(factorial(N))