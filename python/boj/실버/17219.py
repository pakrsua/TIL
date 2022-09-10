# 17219 비밀번호 찾기
import sys

N, M = map(int, sys.stdin.readline().split())
passwordList = {}

for n in range(N):
    site ,password = sys.stdin.readline().split()
    passwordList[site] = password

# print(passwordList)

for m in range(M):
    site = sys.stdin.readline().strip()
    print(passwordList[site])