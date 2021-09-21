# 달팽이는 올라가고 싶다

A, B, V = map(int, input().split())  # A 올라가는 거리 B 미끄러지는 거리 V 나무 길이
day = (V-A) // (A-B)

print(day)