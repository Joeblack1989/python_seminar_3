# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform, randrange

my_list = [1.1, 1.2, 3.1, 5, 10.01]
new_list = [round(val%1, 2) for val in my_list if isinstance(val, float)]

print(new_list)
print(max(new_list) - min(new_list))