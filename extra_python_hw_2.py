Task_1

a = 3
b = 4
operation = input()
if operation == '+':
    print(a + b)
elif operation == '-':
   print(a - b)
elif operation == '*':
    print(a * b)
elif operation == '/':
    print(a / b)
else:
    print("Неизвестно")

Task_2
2.1

count = 0
n = 56742
while n % 10 > 0:
    last_digit = n % 10
    count = count + last_digit
    n = n // 10
print(count)

2.2

count = 0
n = 56742
for i in range(5):
    last_digit = n % 10
    count = count + last_digit
    n = n // 10
print(count)

2.3

count = 1
n = 56742
while n % 10 > 0:
    last_digit = n % 10
    count = count * last_digit
    n = n // 10
print(count)

2.4

count = 1
n = 56742
for i in range(5):
    last_digit = n % 10
    count = count * last_digit
    n = n // 10
print(count)

Task_3

3.1

n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

3.1

total = 0
n = 12
for i in range(1, n + 1):
    if n % i == 0:
        total += i
print(total)

3.1

product = 1
n = 12
for i in range(1, n + 1):
    if n % i == 0:
        product *= i
print(product)

Task_4

a = 'python is good'
b = 'hello all'
s = a + b
index = 0
while True:
    if s[index] != 'a':
        print("Текущая буква:", s[index])
        index += 1
    elif s[index] == 'a':
        print("Ага! Нашлась")
        break
    if index == len(s) and 'a' not in s:
        print("Распечатали все буквы")

Task_5

import random
array_1 = []
sum = 0
starting_point = random.randint(5, 12)
for number in range(starting_point, starting_point + 12, 2):
    array_1.append(number)
    sum += number
    avg = sum / 6
array_2 = [array_1[0], array_1[5], avg, sum]
array_3 = ['min', 'max', 'avg', 'sum']
my_dict = dict(zip(array_3, array_2))
print(my_dict)

Task_6

my_array = []
n = random.randint(5, 9)
for num in range(n, n ** 2 + 1):
    if num % 2 != 0:
        my_array.append(num)
print(my_array)

6.1

n = random.randint(5, 9)
for num in range(n, n ** 2 + 1):
    if num % 2 != 0:
        print(num, end='*')

