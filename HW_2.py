item_1 = 5
item_2 = 7
result_sum = item_1 + item_2
print('result_sum =', result_sum)
result_subtr = item_1 - item_2
print('result_subtr =', result_subtr)
result_multi = item_1 * item_2
print('result_multi =', result_multi)
result_exp = item_1 ** item_2
print('result_exp =', result_exp)

import math

result_m_exp = math.pow(item_1, item_2)
print('result_m_exp =', result_m_exp)
result_s_root = math.sqrt(item_2)
print('result_s_root', result_s_root)
result_mp_s_root = math.pow(item_2, 0.5)
print('result_mp_s_root =', result_mp_s_root)
#19. Присвоить переменной item_1 odd значение
item_1 = 11
#20. Присвоить переменной item_2 even значение
item_2 = 8
#21. Создать переменную result_division в которой вы разделите item_1 на item_2.
result_division = item_1 / item_2
# 22. Вывести result_division в консоль.
print('result_division =', result_division)
# 23. Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.
result_m_floor = math.floor(result_division)
#24. Вывести result_m_floor в консоль.
print('result_m_floor =', result_m_floor)
#25. Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.
result_m_ceil = math.ceil(result_division)
#26. Вывести result_m_ceil в консоль
print('result_m_ceil =', result_m_ceil)
#27. Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
result_int = int(result_division)
#28. Вывести result_int в консоль.
print('result_int =', result_int)
#29. Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
result_no_division_loss = item_1 // item_2
#30. Вывести result_no_division_loss в консоль.
print('result_no_division_loss =', result_no_division_loss)
#31. Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
result_division_loss = item_1 % item_2
#32. Вывести result_division_loss в консоль.
print('result_division_loss =', result_division_loss)
#33. Создать переменную item_3 и присвоить ей целое число
item_3 = 10
#34. Прибавить 10 к item_3 с присвоением.
item_3 += 10
#35. Вывести item_3 в консоль.
print(item_3)
#36. Отнять 5 от item_3 с присвоением.
item_3 -= 5
#37. Вывести item_3 в консоль.
print(item_3)
#38. Умножить item_3 на 3 с присвоением.
item_3 *= 3
#39. Вывести item_3 в консоль.
print(item_3)
#40. Разделить item_3 на 2 с присвоением.
item_3 /= 2
#41. Вывести item_3 в консоль.
print(item_3)
#42. Возвести в степень 2 item_3 с присвоением.
item_3 **= 2
#43. Вывести item_3 в консоль.
print(item_3)
#44. Найти квадратный корень item_3 с присвоением.
item_3 **= 0.5
#45. Вывести item_3 в консоль.
print(item_3)
#46. Присвоить остаток от деления item_3
item_3 %= 2
#47. Вывести item_3 в консоль.
print(item_3)

#48. Создать переменную b_item_t и присвоить True
b_item_t = True
#49. Создать переменную b_item_f и присвоить False
b_item_f = False
#50. Создать переменную b_item_relult_sum и присвоить сумму b_item_t и b_item_f
b_item_result_sum = b_item_t + b_item_f
#51. Вывести b_item_relult_sum в консоль.
print('b_item_result_sum =', b_item_result_sum)
#52. Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f
b_item_result_substr = b_item_t - b_item_f
#53. Вывести b_item_relult_subtr в консоль.
print('b_item_result_substr =', b_item_result_substr)
#54. Создать переменную b_item_relult_multi и присвоить умножение b_item_t и b_item_f
b_item_result_multi = b_item_t * b_item_f
#55. Вывести b_item_relult_multi в консоль.
print('b_item_result_multi =', b_item_result_multi)
# 56. Создать переменную b_item_relult_division и присвоить деление b_item_t и b_item_f. # 57. Вывести b_item_relult_division в консоль.
try:
    b_item_result_division = b_item_t / b_item_f
except ZeroDivisionError:
    print('Делить на 0 нельзя')
#58. Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int
b_item_1_int = int(b_item_t)
# 59. Вывести b_item_1_int в консоль.
print(b_item_1_int)
#60. Создать переменную b_item_2_int и присвоить явное приведение b_item_2 к int
b_item_2_int = int(b_item_f)
#61. Вывести b_item_2_int в консоль
print(b_item_2_int)
