# 10815 숫자 카드
import sys

N = int(sys.stdin.readline())
mycard = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
mycard.sort()
# 출력할 배열
visited = [0] * M

for i in range(M):
    start = 0
    end = N - 1
    # print(visited)
    # start의 값이 end 와 같거나 작은 동안 실행
    # start가 end 보다 커지면 반복문 실행 중지
    while start <= end:
        mid = (start + end) // 2
        if card[i] == mycard[mid]:
            visited[i] = 1
            break
        # 값이 작은 경우 처음 부터 mid 앞숫자까지 탐색하므로 mid -1 해준다
        # [0 0 0 mid 0 0 0]
        elif card[i] < mycard[mid]:
            end = mid - 1
        else:
            start = mid + 1
print(*visited)