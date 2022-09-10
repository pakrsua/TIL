# 14499. 주사위 굴리기

dr = [0, 0, -1, 1]# 동서북남
dc = [1, -1, 0, 0]

n, m , x, y ,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

