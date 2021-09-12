# 다이얼

alpa = input()

num = {2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'], 5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'], 8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z']}

time = 0

for i in alpa:
    for key, value in num.items():
        for k in value:
            if k == i:
                # print(key,end='')
                time += key+1
# print()
print(time)