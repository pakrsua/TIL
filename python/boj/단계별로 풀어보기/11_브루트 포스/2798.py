# 블랙잭
# 조합을 만들어서 풀어야 겠다
def comb(idx, s_idx):
    global ans
    if s_idx == 3:
        add = 0
        for i in get_list:
            add += i
        sub = M - add
        if sub < 0 :
            sub * -1
        elif M-ans > sub:
            ans = add
        # print(get_list)
        return
    elif idx == N:
        return
    else:
        get_list[s_idx] = card_list[idx]
        comb(idx+1, s_idx+1)
        comb(idx+1, s_idx)

N, M = map(int, input().split())
card_list = list(map(int,input().split()))
get_list = [0] * 3
ans = 0
comb(0, 0)
print(ans)