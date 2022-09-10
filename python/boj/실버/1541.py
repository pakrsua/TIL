# 1541 잃어버린 괄호

# '-'를 기준으로 나누어 입력받는다
num = list(map(str,input().split('-')))
# print(num)

# 최종적으로 빼지는 수들이 들어올 리스트
arr = []

for i in range(len(num)):
# 만약 list 안에 수가 정수로 변환이 가능하다면 arr 리스트로 들어오고
# +를 포함한 문자라 변환이 되지 않을 경우 except로 이동한다
    try:
        arr.append(int(num[i]))
    except:
        add_ans = 0
        add = []
        add += num[i].split('+')
# +를 기점으로 수를 더해준다
        for j in add:
            add_ans += int(j)
            # print(j)
# 더해진 수를 arr 리스트로 보낸다
        arr.append(int(add_ans))

# 최종적으로 arr 리스트에 있는 수들을 모두 빼준다.
ans = arr[0]
for i in range(1,len(arr)):
    ans -= arr[i]
print(ans)