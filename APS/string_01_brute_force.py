#고지식한 패턴정렬

#하나씩 처음부터 끝까지 차례대로 순회하면서 문자를 일일이 비교

str1 = input()
str2 = input()
 
    #고지식...
idx_str1 = 0
idx_str2 = 0
 
while idx_str1 < len(str1) and idx_str2 < len(str2):
    if str2[idx_str2] != str1[idx_str1]:
        idx_str2 = idx_str2 -idx_str1
        idx_str1 = -1
    idx_str2 += 1
    idx_str1 += 1
if idx_str1 == len(str1):
    print('y')
else:
    print('n')