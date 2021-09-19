# 초심자의 회문 검사

def palindrome(word):
    if word == word[::-1]:
        return 1

    else:
        return 0


test_case = int(input())

for i in range(test_case):
    word = input()

    print(f'#{i + 1}', end=' ')

    print(palindrome(word))