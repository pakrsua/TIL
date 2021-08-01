list_method = dir(list)
#리스트 정리
##print(list_method) 아래 실행결과
'''
'__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', 
'__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',

'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

'''

my_list = [1,3,5,7,9,8,4,6,2]

#
#append 리스트 요소 추가
my_list.append(10)
print(my_list)
#[1, 3, 5, 7, 9, 8, 4, 6, 2, 10]

#
#copy 리스트 복사
my_list_2 = my_list.copy()
print(my_list_2)
#[1, 3, 5, 7, 9, 8, 4, 6, 2, 10]

#복사된 리스트 변경해보기
my_list_2[0] = 11
print(my_list_2)
#[11, 3, 5, 7, 9, 8, 4, 6, 2, 10]
print(my_list)
#[1, 3, 5, 7, 9, 8, 4, 6, 2, 10]
# -> .copy()를 통해 복사한 리스트는 다른 id 값을 가지고 있어서 복사본의 변경이 영향을 미치지 않는다

#
#count(인자) 리스트가 가지고 있는 인자의 갯수 세기
print(my_list.count(1))
#1

#
#extend(iterable) 리스트의 뒤에 iterable(순서가 있는)항목을 추가해준다
my_list.extend(my_list_2)
print(my_list)
#[1, 3, 5, 7, 9, 8, 4, 6, 2, 10, 11, 3, 5, 7, 9, 8, 4, 6, 2, 10]

#
#index() 입력된 인자의 위치를 반환
print(my_list.index(1))
#0

#
#insert(x,y) x자리에 y를 입력해줌
my_list.insert(0,30)
print(my_list)
#[30, 1, 3, 5, 7, 9, 8, 4, 6, 2, 10, 11, 3, 5, 7, 9, 8, 4, 6, 2, 10]

#
#pop(x) 입력된 값을 빼줌
my_list.pop(11)
print(my_list)
#[30, 1, 3, 5, 7, 9, 8, 4, 6, 2, 10, 3, 5, 7, 9, 8, 4, 6, 2, 10]
my_list.pop()#()안에 입력을 하지 않으면 마지막 값을 빼준다
print(my_list)
#[30, 1, 3, 5, 7, 9, 8, 4, 6, 2, 10, 3, 5, 7, 9, 8, 4, 6, 2]

#
#remove(x) 입력된 값을 빼줌 값이 없으면 에러를 일으킨다
my_list.remove(10)
print(my_list)
#[30, 1, 3, 5, 7, 9, 8, 4, 6, 2, 3, 5, 7, 9, 8, 4, 6, 2]

# my_list.remove(100)
# print(my_list)
#my_list.remove(100)
#ValueError: list.remove(x): x not in list

#
#sort() 리스트를 정렬해준다
my_list.sort()
print(my_list)
#[1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 30]

# 숫자 리스트가 문자로 되어 있는 경우
my_list_3 = ['1', '2', '3', '5', '10', '11', '12', '22', '33', '34']
my_list_3.sort()
print(my_list_3)
#['1', '10', '11', '12', '2', '22', '3', '33', '34', '5']

#
#reverse()리스트를 뒤집어서 출력해준다
my_list.reverse()
print(my_list)
#[30, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1]

#
#clear()리스트 항목 삭제(리스트 자체 삭제x)
my_list.clear()
print(my_list)
#[]