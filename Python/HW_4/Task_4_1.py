''' Задача №4       Процедурный вид

======= Обменник =======

Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
    1. Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
    2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
    3. Потом Скрипт выводит "Введите сумму"
    4. Пользователь вводит сумму int
    5. Скрипт выводит:
            "Вы ввели сумму int и валюту "Валюта" "
            "конвертированная сумма в "Валюта" = int"
    6. Скрипт должен выдать сообщение
                "Введите положительное число." Если число меньше 0.
                "Вы ввели не число. Введите число." Если введены буквы.
                "Вы ввели пустое поле. Введите число." Если введено пустое значение.
    7. После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.

'''

while True:

    print("====================================")
    input_currency = input("Выберите валюту: \n USD \n EUR \n CHF \n GBP \n CNY \n")
    input_money = input("Введите сумму: ")

    try:
        if int(input_money) > 0:
            print("====================================")
            if input_currency == "USD" or input_currency == "usd":
                input_money_USD = int(input_money) / 2.50
                print("Вы ввели сумму ", input_money, "BYN и валюту \"",  input_currency, "\"")
                print("Конвертированная сумма в USD = ", round(input_money_USD, 2))
            if input_currency == "EUR" or input_currency == "eur":
                input_money_EUR = int(input_money) / 2.95
                print("Вы ввели сумму ", input_money, "BYN и валюту \"", input_currency, "\"")
                print("Конвертированная сумма в EUR = ", round(input_money_EUR, 2))
            if input_currency == "CHF" or input_currency == "chf":
                input_money_CHF = int(input_money) / 2.71
                print("Вы ввели сумму ", input_money, "BYN и валюту \"", input_currency, "\"")
                print("Конвертированная сумма в CHF = ", round(input_money_CHF, 2))
            if input_currency == "GBP" or input_currency == "gbp":
                input_money_GBP = int(input_money) / 3.46
                print("Вы ввели сумму ", input_money, "BYN и валюту \"", input_currency, "\"")
                print("Конвертированная сумма в GBP = ", round(input_money_GBP, 2))
            if input_currency == "CNY" or input_currency == "cny":
                input_money_CNY = int(input_money) / 0.38
                print("Вы ввели сумму ", input_money, "BYN и валюту \"", input_currency, "\"")
                print("Конвертированная сумма в CNY = ", round(input_money_CNY, 2))

        elif int(input_money) < 0:
            print("Введите положительное число.")
        else:
            print("Вы ввели 0. Введите число.")
    
    except:
        if input_money == "":
            print("Вы ввели пустое поле. Введите число.")
        else:
            print("Вы ввели не число. Введите число.")