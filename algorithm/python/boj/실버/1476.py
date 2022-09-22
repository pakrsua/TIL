# 1476 날짜 계산

# 입력받음
E,S,M = map(int,input().split())
# 더해질 함수 초기화
e = s = m = 0
# 값
cnt = 0

# 계속 반복
while True:
    e += 1
    # 15 넘어가면 1로 돌아옴
    if e > 15:
        e = 1
    s += 1
    # 28 넘어가면 1로 돌아옴
    if s > 28:
        s = 1
    m += 1
    # 19 넘어가면 1로 돌아옴
    if m > 19:
        m = 1
    cnt += 1
    # 입력값과 같을 때 반복문 탈출
    if e == E and s == S and m == M:
        break

print(cnt)