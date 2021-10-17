''' Задача №3  Процедурный вид

===== Обменник ======

Создать скрипт, который будет запускаться из консоли 1 раз, выдавать результат и зарываться.
    1. На вход обменнику вводишь количество денег int.
    2. На выходе в консоль выводится отввет в таком виде:
                "Вы ввёли int (Валюта)"
                "конвертированная сумма в USD = int"
                "конвертированная сумма в EUR = int"
                "конвертированная сумма в CHF = int"
                "конвертированная сумма в GBP = int"
                "конвертированная сумма в CNY = int"

    3. Скрипт должен выдать сообщение
                "Введите положительное число." Если число меньше 0.
                "Вы ввели не число. Введите число." Если введены буквы.
                "Вы ввели пустое поле. Введите число." Если введено пустое значение.
    4. Валюту пользователя определите сами.
'''


input_money_BYN = input("Введите сумму для конвертации: ")

try:
    if int(input_money_BYN) > 0:
        input_money_USD = int(input_money_BYN) / 2.50
        input_money_EUR = int(input_money_BYN) / 2.95
        input_money_CHF = int(input_money_BYN) / 2.71
        input_money_GBP = int(input_money_BYN) / 3.46
        input_money_CNY = int(input_money_BYN) / 0.38

        print("Вы ввели ", input_money_BYN, " BYN")
        print("Конвертированная сумма в USD = ", round(input_money_USD, 2))
        print("Конвертированная сумма в EUR = ", round(input_money_EUR, 2))
        print("Конвертированная сумма в CHF = ", round(input_money_CHF, 2))
        print("Конвертированная сумма в GBP = ", round(input_money_GBP, 2))
        print("Конвертированная сумма в CNY = ", round(input_money_CNY, 2))
    elif int(input_money_BYN) < 0:
        print("Введите положительное число.")
    else:
        print("Вы ввели 0. Введите число.")

except:
    if input_money_BYN == "":
        print("Вы ввели пустое поле. Введите число.")
    else:
        print("Вы ввели не число. Введите число.")