# 벌집

# num = int(input())
# room = 0
# while True:
#     if num < room * 6:
#         break
#     room += 1
#
# print(room)

num = int(input())
room = 1
cnt = 1
while num > room:
    room = (cnt * 6)+1
    cnt += 1
print(cnt)