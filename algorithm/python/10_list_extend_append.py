
my_list_1 = [1, 2, 3]
my_list_2 = [4, 5, 6]

my_list_1.append(my_list_2)
print(my_list_1)
# [1, 2, 3, [4, 5, 6]]

my_list_1.append(4)
print(my_list_1)
# [1, 2, 3, 4]

my_list_1.extend(my_list_2)
print(my_list_1)
# [1, 2, 3, 4, 5, 6]

my_list_1.extend(4)
print(my_list_1)
# my_list_1.extend(4)
# TypeError: 'int' object is not iterable


my_list_3 = ['apple', 'banana']
my_list_4 = ['coffe', 'milk']

my_list_3.append(my_list_4)
print(my_list_3)
# ['apple', 'banana', ['coffe', 'milk']]
my_list_3.append('grape')
print(my_list_3)
# ['apple', 'banana', 'grape']


my_list_3.extend(my_list_4)
print(my_list_3)
# ['apple', 'banana', 'coffe', 'milk']
my_list_3.extend('grape')
print(my_list_3)
# ['apple', 'banana', 'g', 'r', 'a', 'p', 'e']