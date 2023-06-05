# ✔ Напишите функцию для транспонирования матрицы

def transpon_matrix(matrix: list[list:int]) -> list[list:int]:
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


print(transpon_matrix([[1, 2], [5, 6], [10, 12]]))



