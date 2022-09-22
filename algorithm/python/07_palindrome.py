#회문 만들어보기


# [::-1] 로 문자열 뒤집어서 만들기


##############################
def palindrome(word):
    if word == word[::-1]:
        return 1

    else:
        return -1
        
test_case = int(input())#테스트케이스가 몇개 들어오는지 받기

for i in range(test_case):
    word = input()
    
    print(f'#{i+1}', end = ' ')
    
    print(palindrome(word))
#################################
#테스트 케이스 없이

# word = input()

# print(palindrome(word))