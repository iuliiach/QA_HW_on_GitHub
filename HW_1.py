#1) Создать переменную типа String
a = 'apple'
#2) Создать переменную типа Integer
b = 15
#3) Создать переменную типа Float
c = 4.78
#4) Создать переменную типа Bytes
d = b'welcome to python'
#5) Создать переменную типа List
e = ['cat', 'dog', 'hamster']
#6) Создать переменную типа Tuple
f = ('ginea pig', 'parrot', 'rat')
#7) Создать переменную типа Set
my_set_1 = {'summer', 'autumn', 'winter', 'spring'}
#8) Создать переменную типа Frozen set
my_set_2 = frozenset({15, 'days', 'months', 8})
#9) Создать переменную типа Dict
my_dict = {'student1': 'Ann', 'student2': 'Ben', 'student3': 'James'}
#10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)
print(type(f), f)
print(type(my_set_1), my_set_1)
print(type(my_set_2), my_set_2)
print(type(my_dict), my_dict)
#11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
str_1 = 'God_is_'
str_2 = 'Love'
str_3 = str_1 + str_2
print(str_3)
#12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(a, b, str_3)
#13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(a + str(b) + str_3)
