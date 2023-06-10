import random

SIZE = 8


def chess_board(x: list[int], y: list[int]) -> bool:
    for i in range(SIZE):
        for j in range(i + 1, SIZE):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
    return True


def chess_board_2() -> dict[list[int]:list[int]]:
    x = [1, 2, 3, 4, 5, 6, 7, 8]
    y = [1, 2, 3, 4, 5, 6, 7, 8]
    chess_board_dict = {}
    count = 1
    while len(chess_board_dict) < 4:
        random.shuffle(x)
        random.shuffle(y)
        for i in range(SIZE):
            for j in range(i + 1, SIZE):
                if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                    continue
        chess_board_dict.setdefault(count, [x, y])
        count += 1
    return chess_board_dict