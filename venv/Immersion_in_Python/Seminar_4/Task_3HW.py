# ✔ Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.
import datetime

MULTIPLE: int = 50
COMMISION = 0.015
BONUS = 1.03
TAX = 0.9
MIN_COMMISION: int = 30
MAX_COMMISION: int = 600
TAX_RICH: int = 5000000

balance = 0
count_operation = 0
log = {}


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
        log_cash(f'Операция пополнение: Баланс: {balance} - внесенные наличные: {cash}')
    else:
        log_cash('Операция пополнение: Неккоректная сумма для пополнения')
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
            balance = balance - cash - MIN_COMMISION
            log_cash(f'Операция снятие: Баланс: {balance} - снятые наличные: {cash} - комиссия: {MIN_COMMISION} ')
        elif commision_cash_out >= MAX_COMMISION:
            balance = balance - cash - MAX_COMMISION
            log_cash(f'Операция снятие: Баланс: {balance} - снятые наличные: {cash} - комиссия: {MAX_COMMISION} ')
        else:
            balance = balance - cash - commision_cash_out
            log_cash(f'Операция снятие: Баланс: {balance} - снятые наличные: {cash} - комиссия: {commision_cash_out} ')
        if count_operation > 3:
            balance *= BONUS
            log_cash(f'Операция снятие: Начисление бонуса на остаток: {balance}')
    else:
        log_cash('Операция снятие: Недостаточно средств')
        print('Недостаточно средств')


def log_cash(operation: str):
    global log
    log.setdefault(datetime.datetime.now(), operation)


while True:
    msg = input('Введите одну из команжы: cash_in, cash_out, exit, log - ')
    match msg:
        case 'cash_in':
            numbers = int(input('Введите сумму для пополнения: '))
            cash_in(numbers)
        case 'cash_out':
            numbers = int(input('Введите сумму для снятия: '))
            cash_out(numbers)
        case 'log':
            for key, value in log.items():
                print(f'{key} - {value}')
        case 'exit':
            print(f"Баланс: {str(balance)}")
            break
    print(f"Баланс: {str(balance)}")
