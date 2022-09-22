# 10867 중복 빼고 정렬하기

N = int(input())
nums = list(map(int,input().split()))

set_nums = set(nums)
nums = list(set_nums)

nums.sort()

print(*nums)