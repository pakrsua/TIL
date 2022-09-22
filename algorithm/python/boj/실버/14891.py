# 14891. 톱니바퀴

# 돌리기
def spin(num,dir):
    #시계방향
    if dir == 1:
        gears[num-1].insert(0,gears[num-1][-1])
        gears[num-1].pop()
    #반시계방향
    else:
        gears[num-1].append(gears[num-1][0])
        gears[num-1].pop(0)

# 톱니 돌리기
def all(num,dir):
    # 오른쪽, 왼쪽 탐색
    # 만약 왼쪽에 톱니가 있다면
    if num-1 > 0:
        # 그리고 그 톱니가 다른 극을 가지고 있고, 아직 돈적이 없다면
        if gears[num-2][2] != gears[num-1][6] and visited[num-2] == 0:
            if dir == 1:
                # 원래 방향과 반대로 돌기
                gears[num - 2].append(gears[num - 1][0])
                gears[num - 2].pop(0)
                dir = -1
            elif dir == -1:
                gears[num - 2].insert(0, gears[num - 1][-1])
                gears[num - 2].pop()
                dir = 1
            visited[num-2] = 1
            all(num-1, dir)
        else:
            return
    if num-1 < 3:
        if gears[num][6] != gears[num - 1][2] and visited[num] == 0:
            if dir == 1:
                # 반대로
                gears[num].append(gears[num - 1][0])
                gears[num].pop(0)
                dir = -1
            elif dir == -1:
                gears[num].insert(0, gears[num - 1][-1])
                gears[num].pop()
                dir = 1
            visited[num] = 1
            all(num + 1, dir)
        else:
            return
    return


gears = [list(map(int,input())) for _ in range(4)]

k = int(input())

for tc in range(k):
    visited = [0] * 4
    num, dir = map(int, input().split())
    # 일단 돌릴 톱니 visited 체크해두기(all 함수에서 안돌아가게 하기 위해서)
    visited[num-1] = 1
    # 다른 톱니부터 먼저 돌리기
    all(num, dir)
    # 해당 톱니 돌리기
    spin(num, dir)

# 마지막 점수 계산하기
ans = 0
x = 1
for i in range(4):
    ans += gears[i][0] * x
    x = x * 2

# 예제 1번은 맞는데 3,4번이 틀렸더라구요ㅠㅇㅠ
print(ans)
