def puncher(n):
    for i in range(n):
        for j in range(n):
            if i%3 == 1 and j%3 == 1:
                star_arr[i][j] = ' '
N = int(input())
star_arr = [list('*'*N) for _ in range(N)]
print(star_arr)
puncher(N)
print(star_arr)