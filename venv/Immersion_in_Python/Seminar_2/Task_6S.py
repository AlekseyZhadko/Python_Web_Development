# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ Нельзя снять больше, чем на счёте
# ✔ Любое действие выводит сумму денег
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%


MULTIPLE: int = 50
COMMISION = 0.015
BONUS = 1.03
TAX = 0.9
MIN_COMMISION: int = 30
MAX_COMMISION: int = 600
TAX_RICH: int = 5000000

balance = 0
count_operation = 0


def cash_in(cash: int):
    global balance
    global count_operation
    if balance >= TAX_RICH:
        balance *= TAX
    if cash % MULTIPLE == 0:
        count_operation += 1
        balance += cash
        if count_operation > 3:
            balance *= BONUS
    else:
        print('Неккоректная сумма для пополнения')


def cash_out(cash: int):
    global balance
    global count_operation
    if balance >= TAX_RICH:
        balance *= TAX
    commision_cash_out = cash * COMMISION
    if balance >= commision_cash_out + cash:
        count_operation += 1
        if commision_cash_out <= MIN_COMMISION:
            balance -= cash - MIN_COMMISION
        elif commision_cash_out >= MAX_COMMISION:
            balance -= cash - MAX_COMMISION
        else:
            balance -= cash - commision_cash_out
        if count_operation > 3:
            balance *= BONUS
    else:
        print('Недостаточно средств')


while True:
    msg = input('Введите одну из команжы: cash_in, cash_out, exit - ')
    match msg:
        case 'cash_in':
            cash = int(input('Введите сумму для пополнения: '))
            cash_in(cash)
        case 'cash_out':
            сash = int(input('Введите сумму для снятия: '))
            cash_out(cash)
        case 'exit':
            print(f"Баланс: {str(balance)}")
            break
    print(f"Баланс: {str(balance)}")
