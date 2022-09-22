#숫자 두 개를 입력받아서 가로n 세로m 상자만들기

#이중 for문

n = int(input())
m = int(input())

for i in range(0,m):
    for j in range(0,n):
        print('*', end ='')#, end = ''로 n의 값 가로로 출력
    print()#m 만큼 줄 바꾸기

#한줄로 입력
print()
#이스케이프 시퀀스 활용
print(('*' * n +'\n') * m)
        