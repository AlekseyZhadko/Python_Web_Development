import Task_4_1S

_ANSWEARS = dict()


def new_mistery(misterys: dict, try_count: int):
    for key, value in misterys.items():
        count = Task_4_1S.mistery(key, value, try_count)
        if count:
            _ANSWEARS[key] = f"Угадано за {count} раз(а)"
            print(f"Угадано за {count} раз(а)")
        else:
            _ANSWEARS[key] = "Не угадали"
            print("Не угадали")


def show_dict():
    print(*(f"{key} - {value} \n" for key, value in _ANSWEARS.items()))
