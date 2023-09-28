from math import ceil
from random import randint


# Расчет размера квадрата Полибия
def count_matrix_size(alphabed):
    size = ceil(len(alphabed) ** 0.5)
    assert size == len(alphabed) ** 0.5, "Некорректный алфавит"
    return size


# Получение изначальной матрицы
def get_default_matrix(matrix_size):
    matrix = [''] * matrix_size
    for i in range(matrix_size):
        matrix[i] = [''] * matrix_size
    return matrix


# Создание квадрата полибия по заданному алфавиту
def configure_matrix(alphabed):
    # Ищем размер итогового квадрата
    matrix_size = count_matrix_size(alphabed)

    # Инициализируем квадрат
    matrix = get_default_matrix(matrix_size)

    current_alphabed = list(alphabed)

    # Заполняем матрицу случайными символами из алфавита
    for i in range(matrix_size):
        for j in range(matrix_size):
            if len(current_alphabed) > 0:
                current_idx = randint(0, len(current_alphabed) - 1)
                current_symbol = current_alphabed[current_idx]
                matrix[i][j] = current_symbol
                del current_alphabed[current_idx]

    return matrix


# Конвертирование квадрата Полибия в строку
def convert_matrix_to_string(matrix):
    result = ""

    for i in range(len(matrix)):
        for j in range(len(list(matrix[i]))):
            result += matrix[i][j]
        if len(matrix) - 1 != i:
            result += "|"

    return result
