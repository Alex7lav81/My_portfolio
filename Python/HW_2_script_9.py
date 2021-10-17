""" Задание 9

Написать скрипт используя функцию input().
     1. Функция должна на вход принимать целое число.
     2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100))
     3. Выводить должна "Вы вели число = (введённое число), которое (меньше/больше/равно и меньше/больше/равно)
     сгенерированному числу"
"""

import random
print("Введите целое число:")
var_int = int(input())
var_rand_1 = random.randint(1, 100)
var_rand_2 = random.randint(1, 100)

if var_int > var_rand_1:
    if var_int > var_rand_2:
        print("Вы ввели чмсло = ", var_int, ", которое больше ", var_rand_1, " и больше ", var_rand_2)
    elif var_int < var_rand_2:
        print("Вы ввели чмсло = ", var_int, ", которое больше ", var_rand_1, " и меньше ", var_rand_2)
    else:
        print("Вы ввели чмсло = ", var_int, ", которое больше ", var_rand_1, " и равно ", var_rand_2)
elif var_int < var_rand_1:
    if var_int > var_rand_2:
        print("Вы ввели чмсло = ", var_int, ", которое меньше ", var_rand_1, " и больше ", var_rand_2)
    elif var_int < var_rand_2:
        print("Вы ввели чмсло = ", var_int, ", которое меньше ", var_rand_1, " и меньше ", var_rand_2)
    else:
        print("Вы ввели чмсло = ", var_int, ", которое меньше ", var_rand_1, " и равно ", var_rand_2)
else:
    if var_int > var_rand_2:
        print("Вы ввели чмсло = ", var_int, ", которое равно ", var_rand_1, " и больше ", var_rand_2)
    elif var_int < var_rand_2:
        print("Вы ввели чмсло = ", var_int, ", которое равно ", var_rand_1, " и меньше ", var_rand_2)
    else:
        print("Вы ввели чмсло = ", var_int, ", которое равно ", var_rand_1, " и равно ", var_rand_2)