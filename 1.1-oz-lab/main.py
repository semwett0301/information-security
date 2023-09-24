from utils.io import input_from_file, input_alphabed, input_mode, input_matrix, input_matrix_from_file, Mode, \
    print_result, output_result, input_save_matrix, output_matrix, print_matrix
from utils.utils import configure_matrix, convert_matrix_to_string

mode = input_mode()
alphabed = input_alphabed()

if mode == Mode.CR:
    if not input_matrix():
        matrix = configure_matrix(alphabed)
    else:
        matrix = input_matrix_from_file(alphabed)
else:
    matrix = input_matrix_from_file(alphabed)

# Поиск координат символа в квадрате Полибия
def find_idx_in_matrix(char):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == char:
                return [i, j]

    print(char)
    raise ValueError("Некорректная матрица (не содержит весь алфавит)")

# Циклический сдвиг строки
def cyclic_shift(value, mode="STRAIGHT"):
    value = list(value)

    if mode != "REVERSE":
        value = value[::-1]

    last_char = value.pop()
    value.append(last_char)

    return value if mode == "REVERSE" else value[::-1]

# Получение индексов в квадрате Полибия в виде x и y координат
def get_indexes_from_matrix(value):
    x_idxs = []
    y_idxs = []

    for char in value:
        i, j = find_idx_in_matrix(char)
        x_idxs.append(i)
        y_idxs.append(j)

    return x_idxs, y_idxs

# Получение индексов в квадрате Полибия по строке
def get_indexes_by_str(value):
    x_idxs, y_idxs = get_indexes_from_matrix(value)

    result = ""

    for char in x_idxs:
        result += str(char)

    for char in y_idxs:
        result += str(char)

    return list(result)

# Получение строки по индексам в квадрате Полибия
def get_str_by_indexes(indexes):
    result = ""

    for i in range(len(indexes) // 2):
        result += matrix[int(indexes[i * 2])][int(indexes[i * 2 + 1])]

    return result

# Получение индексов из зашифрованной строки
def get_res_indx(value):
    source_indexes = ""

    x_indx, y_indx = get_indexes_from_matrix(value)
    for i in range(len(value)):
        source_indexes += str(x_indx[i]) + str(y_indx[i])

    source_indexes = cyclic_shift(source_indexes, "REVERSE")
    x_res_indx = source_indexes[0:len(source_indexes) // 2]
    y_res_indx = source_indexes[len(source_indexes) // 2:]

    return x_res_indx, y_res_indx

# Функция шифрования
def crypto(source):
    source_indexes = get_indexes_by_str(source)
    source_indexes = cyclic_shift(source_indexes)
    return get_str_by_indexes(source_indexes)

# Функция дешифрования
def decrypto(source):
    x_res_indx, y_res_indx = get_res_indx(source)

    result_indx = ""

    for i in range(len(x_res_indx)):
        result_indx += str(x_res_indx[i]) + str(y_res_indx[i])

    return get_str_by_indexes(result_indx)


if mode == Mode.CR:
    string_for_crypto = input_from_file()

    result = crypto(string_for_crypto)

    if input_save_matrix():
        output_matrix(convert_matrix_to_string(matrix))
else:
    string_for_decrypto = input_from_file()
    result = decrypto(string_for_decrypto)

output_result(result)

print_result(result)
print_matrix(matrix)
