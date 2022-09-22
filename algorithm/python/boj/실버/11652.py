# 11652 카드
import sys

N = int(input())
cards = {}

for i in range(N):
    card = int(sys.stdin.readline())
    if card in cards:
        cards[card] += 1
    else:
        cards[card] = 1
# print(cards)
# s_cards = sorted(cards.items(),key=lambda x:x[0])
# s_cards = sorted(cards.items(),key=lambda x:x[1],reverse=True)
s_cards = sorted(cards.items(),key=lambda x:(-x[1],x[0]))

# print(s_cards)
print(s_cards[0][0])