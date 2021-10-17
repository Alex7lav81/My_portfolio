"""
1) Создать 2 переменных типа String с разными значениями
2) Создать 4 переменных типа Integer с разными значениями
3) Создать 3 переменных типа Float с разными значениями
4) Реализовать 15 вариантов сравнения int переменных с операторами >, <, >=, <=, !=. Pезультаты вывести в консоль.
5) Реализовать 9 вариантов сравнения Float переменных с операторами >, <, >=, <=, !=. Pезультаты вывести в консоль.
6) Реализовать 10 вариантов сравнения int переменных с операторами >, <, >=, <=, != и условными
выражениями (end, or, not). Pезультаты вывести в консоль.
"""

str_1 = "Hotel California"
srt_2 = "Eagles"

int_1 = 123
int_2 = 125
int_3 = 45
int_4 = 55

fl_1 = 3.5
fl_2 = 77.1
fl_3 = 123.7

# 15 вариантов сравнения Int переменных:
print("1.1: ", int_1 > int_2)
print("1.2: ", int_2 > int_3)
print("1.3: ", int_3 > int_4)
print("1.4: ", int_4 > int_1)
print("1.5: ", int_4 < int_1)
print("1.6: ", int_3 < int_4)
print("1.7: ", int_2 < int_3)
print("1.8: ", int_1 <= int_2)
print("1.9: ", int_2 >= int_3)
print("1.10: ", int_4 >= int_3)
print("1.11: ", int_4 >= int_1)
print("1.12: ", int_3 <= int_4)
print("1.13: ", int_1 != int_4)
print("1.14: ", int_3 != int_4)
print("1.15: ", int_2 != int_1, "\n")

# 9 вариантов сравнения Float переменных:
print("2.1: ", fl_1 > fl_2)
print("2.2: ", fl_3 > fl_2)
print("2.3: ", fl_2 < fl_3)
print("2.4: ", fl_1 < fl_2)
print("2.5: ", fl_3 >= fl_1)
print("2.6: ", fl_1 >= fl_2)
print("2.7: ", fl_2 <= fl_1)
print("2.8: ", fl_1 != fl_3)
print("2.9: ", fl_2 != fl_3, "\n")

# 10 вариантов сравнения Int переменных:
print("3.1: ", int_1 > int_2 or int_3 > int_4)
print("3.2: ", int_2 > int_1 or int_3 >= int_4)
print("3.3: ", int_4 >= int_3 or int_2 > int_1)
print("3.4: ", int_1 < int_2 and int_4 >= int_3)
print("3.5: ", int_3 != int_4 and int_2 < int_1)
print("3.6: ", int_1 > int_2 and int_4 != int_3)
print("3.7: ", int_1 >= int_3 and int_2 >= int_4)
print("3.8: ", not int_1 < int_2)
print("3.9: ", not int_4 != int_2)
print("3.10: ", not int_1 == int_2, "\n")