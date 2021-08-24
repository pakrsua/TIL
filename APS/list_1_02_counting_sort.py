# 카운팅 정렬

nums = [1, 5, 8, 9, 1, 3, 4, 6, 5, 7, 6, 1, 1, 3, 2]

sort_nums = [0] * len(nums)         #요소들을 정렬해줄 배열을 선언한다
big_num = -1                        #big_num은 요소들 중 가장 큰 값을 의미
for i in nums:
    if big_num < i:
        big_num = i

counts = [0] * (big_num + 1)        #가장 큰 값까지 카운팅 해줄 배열을 선언한다


for i in range(len(nums)):
    counts[nums[i]] += 1            #각 요소의 자리에 (해당 코드의 경우 9까지) 요소의 갯수를 더해준다
print(counts)                       #[0, 4, 1, 2, 1, 2, 2, 1, 1, 1]


for i in range(1, len(counts)):
    counts[i] += counts[i - 1]      # 배열에 누적값 표현
print(counts)                       #[0, 4, 5, 7, 8, 10, 12, 13, 14, 15]

for i in range(len(nums) - 1, -1, -1): # 뒤에서 부터 시행하는 이유는 안정정렬을 위해서
    n = nums[i]
    counts[n] -= 1
    idx = counts[n]
    sort_nums[idx] = n

print(sort_nums)
