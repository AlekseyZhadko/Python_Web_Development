def _check_leap_year(date: str) -> bool:
    CHECK_NORMAL_1 = 4
    CHECK_NORMAL_2 = 100
    CHECK_NORMAL_3 = 400
    year = int(date.split('.')[-1])
    if year % CHECK_NORMAL_1 == 0 and year % CHECK_NORMAL_2 != 0 or year % CHECK_NORMAL_3 == 0:
        return check_month(date, True)
    return check_month(date, False)


def check_year(date: str) -> bool:
    YEARS = range(1, 10000)
    print(date)
    year = int(date.split('.')[-1])
    if year in YEARS:
        return _check_leap_year(date)
    return False


def check_month(date: str, leap_year: bool) -> bool:
    COUNT_MONTH = range(1, 13)
    month = int(date.split('.')[-2])
    if month in COUNT_MONTH:
        if leap_year:
            return check_day(date, 29)
        else:
            return check_day(date, 28)
    return False


def check_day(date: str, leap_year_day: int) -> bool:
    day = int(date.split('.')[-3])
    month = int(date.split('.')[-2])
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            days = range(1, 32)
            if day in days:
                return True
        case 2:
            days = range(1, leap_year_day + 1)
            if day in days:
                return True
        case 4 | 6 | 9 | 11:
            days = range(1, 31)
            if day in days:
                return True
        case _:
            return False


def check_date(date: str):
    if check_year(date):
        print("Дата корректная")
    else:
        print("Дата не корректная")
