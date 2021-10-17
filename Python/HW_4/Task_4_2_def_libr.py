# def main(input_money_BYN):
#     input_money_USD = convert_money_usd(input_money_BYN)
#     print("Конвертированная сумма в USD = ", round(input_money_USD, 2))
#     input_money_EUR = convert_money_eur(input_money_BYN)
#     print("Конвертированная сумма в EUR = ", round(input_money_EUR, 2))
#     input_money_CHF = convert_money_chf(input_money_BYN)
#     print("Конвертированная сумма в CHF = ", round(input_money_CHF, 2))
#     input_money_GBP = convert_money_gbp(input_money_BYN)
#     print("Конвертированная сумма в GBP = ", round(input_money_GBP, 2))
#     input_money_CNY = convert_money_chy(input_money_BYN)
#     print("Конвертированная сумма в CNY = ", round(input_money_CNY, 2))

def main(money, currency):
    if int(money) > 0:
        print("====================================")
        if currency == "USD" or currency == "usd":
            input_money_USD = convert_money_usd(money)
            print("Вы ввели сумму ", money, "BYN и валюту \"", currency, "\"")
            print("Конвертированная сумма в USD = ", round(input_money_USD, 2))
        if currency == "EUR" or currency == "eur":
            input_money_EUR = convert_money_eur(money)
            print("Вы ввели сумму ", money, "BYN и валюту \"", currency, "\"")
            print("Конвертированная сумма в EUR = ", round(input_money_EUR, 2))
        if currency == "CHF" or currency == "chf":
            input_money_CHF = convert_money_chf(money)
            print("Вы ввели сумму ", money, "BYN и валюту \"", currency, "\"")
            print("Конвертированная сумма в CHF = ", round(input_money_CHF, 2))
        if currency == "GBP" or currency == "gbp":
            input_money_GBP = convert_money_gbp(money)
            print("Вы ввели сумму ", money, "BYN и валюту \"", currency, "\"")
            print("Конвертированная сумма в GBP = ", round(input_money_GBP, 2))
        if currency == "CNY" or currency == "cny":
            input_money_CNY = convert_money_cny(money)
            print("Вы ввели сумму ", money, "BYN и валюту \"", currency, "\"")
            print("Конвертированная сумма в CNY = ", round(input_money_CNY, 2))

    elif int(money) < 0:
        print("Введите положительное число.")
    else:
        print("Вы ввели 0. Введите число.")

def get_money():
    input_money = input()
    return input_money

def convert_money_usd(money):
    input_money_USD = int(money) / 2.50
    return input_money_USD

def convert_money_eur(money):
    input_money_EUR = int(money) / 2.95
    return input_money_EUR

def convert_money_chf(money):
    input_money_CHF = int(money) / 2.71
    return input_money_CHF

def convert_money_gbp(money):
    input_money_GBP = int(money) / 3.46
    return input_money_GBP

def convert_money_cny(money):
    input_money_CNY = int(money) / 0.38
    return input_money_CNY
