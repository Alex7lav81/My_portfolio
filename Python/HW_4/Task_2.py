''' Задача №2

===== Обменник =====

Создать скрипт, который будет запускаться из консоли 1 раз, выдавать результат и зарываться.
    1. На вход обменнику вводишь количество денег int.
    2. На выходе в консоль выводится отввет в таком виде:
                "Вы ввёли int (Валюта)"
                "Конвертированная сумма в USD = int"
                "Конвертированная сумма в EUR = int"
                "Конвертированная сумма в CHF = int"
                "Конвертированная сумма в GBP = int"
                "Конвертированная сумма в CNY = int"
    3. Валюту пользователя определите сами.
'''


input_money_BYN = int(input("Введите сумму для конвертации: "))
input_money_USD = input_money_BYN / 2.50
input_money_EUR = input_money_BYN / 2.95
input_money_CHF = input_money_BYN / 2.71
input_money_GBP = input_money_BYN / 3.46
input_money_CNY = input_money_BYN / 0.38

print("Вы ввели ", input_money_BYN, " BYN")
print("Конвертированная сумма в USD = ", round(input_money_USD, 2))
print("Конвертированная сумма в EUR = ", round(input_money_EUR, 2))
print("Конвертированная сумма в CHF = ", round(input_money_CHF, 2))
print("Конвертированная сумма в GBP = ", round(input_money_GBP, 2))
print("Конвертированная сумма в CNY = ", round(input_money_CNY, 2))