# 달팽이는 올라가고 싶다

A, B, V = map(int, input().split())  # A 올라가는 거리 B 미끄러지는 거리 V 나무 길이

day = 0

if (V-A) % (A-B) == 0:
    day = (V - A) // (A - B) + 1
else:
    day = (V - A) // (A - B) + 2
print(day)