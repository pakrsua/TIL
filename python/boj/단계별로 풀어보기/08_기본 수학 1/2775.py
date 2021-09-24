# 2775 부녀회장이 될테야

T = int(input())

for tc in range(T):
    k = int(input())
    n = int(input())
    people = [[0]*(n) for _ in range(k+1)]
    ans = 0
    i = 1
    for height in range(k+1):
        for room in range(n):

            if height == 0:
                people[height][room] = i
                i += 1
            if room == 0:
                people[height][room] = 1
            elif height !=0 and room != 0:
                people[height][room] = people[height-1][room] + people[height][room-1]

    print(people[k][n-1])
