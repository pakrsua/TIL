# 분해합

# 숫자를 입력받기
N = int(input())
# 출력될 값
ans = 0

# 입력 값부터 0으로 거꾸로 돌면서 입력값에서 빼준다
# 거꾸로 도는 이유는 가장 작은 생성자를 구하기 위해서
# 1에서 부터 돌면 가장 큰 생성자를 출력한다.
for i in range(N, 0,-1):
    # 생성자는 입력 받은 수에서 i 만큼을 빼준 수
    make_num = N - i
    # 생성자 자릿수를 리스트로 생성
    make_num_list = list(map(int, str(make_num)))
    # print(make_num_list)
    make_num_list_add = 0
    # 생성된 리스트를 다 더해서 make_num_list 에 넣어줌
    for num in make_num_list:
        make_num_list_add += num
    # print(make_num_list_add)
    # 만약 자릿수를 모두 합한 값과 i(입력받은 수에서 빼준 값)이 같다면
    if make_num_list_add == i:
        # 답은 해당 i 값인 순간의 생성자로 교체
        ans = make_num
        break

print(ans)