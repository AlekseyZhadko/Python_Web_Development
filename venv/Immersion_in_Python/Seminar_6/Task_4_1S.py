def mistery(text: str, answers: list[str], count: int) -> int:
    print(text)
    count_tryint = 0

    while count_tryint < count:
        answer = input("Что это? ")
        if answer in answers:
            count_tryint += 1
            return count_tryint
        count_tryint += 1
    return 0
