# 단어 공부

# text = input()

# 대소문자를 구분하지 않기 때문에 하나로 통합한다
# text.lower()
# max_num = 0
# max_text = ''
#
# for i in text:
#     num = text.count(i)
#     if num > max_num:
#         max_num = num
#         max_text = i
#
# print(max_text)

text = input()

text = text.upper()
text_list = list(set(text))

counts = [0]*(len(text_list))

for i in range(len(text_list)):
    counts[i] = text.count(text_list[i])
max_num = max(counts)
max_num_count =0
# print(text_list)
# print(counts)

for count_num in counts:
    if max_num == count_num:
        max_num_count += 1
if max_num_count == 1:
    print(text_list[counts.index(max_num)])
else:
    print('?')

