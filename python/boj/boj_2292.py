#벌집
#재귀함수로 풀어보기

#while문 풀이

num = int(input())

room = 1
room_cnt = 1

while num > 1:
    if num < room_cnt + (room*6):
        break
    room += 1
    room_cnt += room*6
print(room-1)