#369게임 만들어보기

n = int(input())
game_list = ''
fin = ''

for i in range(1, n+1):
    game_list += (str(i)+' ')
    game = game_list.split(' ')
for i in range(0, n):
    if '3' in game[i] or '6' in game[i] or '9' in game[i]:
        game[i] = '짝'
game.pop(-1)
for i in range(0, n):
    fin += game[i] + ' '
print(fin)