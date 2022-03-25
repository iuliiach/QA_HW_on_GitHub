# Problem 1: Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу размером n×3 состоящую из данного числа (числа отделены одним пробелом).

n = int(input())
for i in range(1, n + 1):
    for j in range(3):
        print(n, end = ' ')
    print()

# Problem 2: Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу размером n × 5, где в i-ой строке указано число i (числа отделены одним пробелом).

n = int(input())
counter = 0
for i in range(1, n + 1):
    counter += 1
    for j in range(5):
        print(counter, end=' ')
    print()

# Problem 3: Дано натуральное число n (n≤ 9). Напишите программу, которая печатает таблицу сложения для всех чисел от 1 до n в соответствии с примером.

n = int(input())
for i in range(1, n + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    print()
  
# Problem 4: Дано натуральное число n. Напишите программу, которая печатает численный треугольник в соответствии с примером:

# 1
# 22
# 333
# 4444
# 55555

n = int(input())
counter = 0
for i in range(1, n + 1):
    counter = counter + 1
    for j in range(i):
        print(counter, end ='')
    print()

# **Problem 5: Дано нечетное натуральное число nn. Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным nn в соответствии с примером:

# *
# **
# ***
# ****
# ***
# **
# *

n = int(input())
m = int((n + 1) / 2)
for i in range(1, m + 1):
    for j in range(i):
        print('*', end='')
    print()
for i in range(m - 1, 0, -1):
    for j in range(i):
        print('*', end='')
    print()  
