#반복 가능한 자료형의 어느 하나라도 참이면 True리턴 하지만 자료형이 비어 있으면 false반환

# 공식문서
def any(iterable):
    for element in iterable:
        if element: #이부분은 자료형이 존재한다는 의미인가부다
            return True
    return False

# 내가 만들었던 코드
def my_any(elements):
    for i in elements:
        if i :
            return False
        else:
            return True

my_list_01 = []
my_list_02 = [1, 2, 3, '4']
my_list_03 = [[], 2, 3, '4']

print(any(my_list_01))
print(any(my_list_02))
print(any(my_list_03))
# false Ture True 반환

print(my_any(my_list_01))
print(my_any(my_list_02))
print(my_any(my_list_03))
# None True False 반환