# ✔ Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

def awards_dict(names: list, salaries: list, award: list):
    print(*([name, salary * award] for name, salary, award in zip(names, salaries, awards)))


names = ["Иван", "Николай", "Пётр"]
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13]
awards_dict(names, salaries, awards)

