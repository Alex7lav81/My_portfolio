''' Задача №4

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

from HW_4.Task_4_2_def_libr import main
from HW_4.Task_4_2_def_libr import get_money

while True:

    print("====================================")
    print("Выберите валюту: \n USD \n EUR \n CHF \n GBP \n CNY \n")
    input_currency = get_money()
    print("Введите сумму: ")
    input_money = get_money()

    try:
        main(input_money, input_currency)

    except:
        if input_money == "":
            print("Вы ввели пустое поле. Введите число.")
        else:
            print("Вы ввели не число. Введите число.")