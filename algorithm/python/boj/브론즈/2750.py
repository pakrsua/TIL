# 2750 수 정렬하기

N = int(input())
nums = []

for t in range(N):
    nums.append(int(input()))

for i in range(N):
    for j in range(i, N):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]



for i in range(N):
    print(nums[i])