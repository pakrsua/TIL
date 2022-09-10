# 2304 창고 다각형

N = int(input())
pillars = []
ans = 0
# 기둥 입력받기
for pillar in range(N):
    L,H = map(int,input().split())
    pillars.append([L,H])
pillars.sort()
# print(pillars)
#가장 높은 기둥의 높이를 저장해둔다
max_h = 0
for i in pillars:
    if i[1] >= max_h:
        max_h = i[1]
# print(max_h)

# 왼쪽부터 지금 기둥 위치보다 높은 기둥을 찾을 때 마다 기둥과 거리 값을 갱신
# ans 에 현재까지의 값을 더해준다
h = pillars[0][1]
w = pillars[0][0]
for i in pillars:
    if i[1] > h and h != max_h:
        ans += h * (i[0] - w)
        h = i[1]
        w = i[0]
        # 가장 높은 기둥을 만나면 반복문을 종료
    elif h == max_h:
        break
# print(ans)
# 오른쪽부터 계산한다
h = pillars[N-1][1]
w = pillars[N-1][0]
for i in range(N-1,-1,-1):
    if pillars[i][1] > h and h != max_h:
        ans += h * (w - pillars[i][0])
        h = pillars[i][1]
        w = pillars[i][0]
        # 가장 높은 기둥을 만나면 반복문 종료
    elif h == max_h:
        break
# print(ans)
# 가장 높은 기둥이 여러개 있을 수 있으니 가장 높은 기둥과 기둥 사이의 넓이를 구한다
highest =[]
for i in pillars:
    if i[1] == max_h:
        highest.append(i[0])
ans += (max(highest) - min(highest) + 1) * max_h

print(ans)