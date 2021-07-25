# 반복가능한 자료형의 모든 요소가 참이면 True를 반환하는 함수

#공식문서
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

#직접 만들었던 코드
def my_all(elements):
    # 내가 직접 짠 코드에서는 해당 부분이 없으면 none을 return 한다
    ####
    if not elements:
        return True
    ####
    for i in elements:
        if not i :
            return False
        else:
            return True


my_list_01 = []
my_list_02 = [1, 2, 3, '4']
my_list_03 = [[], 2, 3, '4']

print(all(my_list_01))
print(all(my_list_02))
print(all(my_list_03))

print(my_all(my_list_01))
print(my_all(my_list_02))
print(my_all(my_list_03))