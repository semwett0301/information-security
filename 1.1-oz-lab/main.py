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


def crypto_func(i, j):
    if i == len(matrix) - 1:
        return matrix[0][j] if matrix[0][j] != "" else crypto_func(0, j)
    else:
        return matrix[i + 1][j] if matrix[i + 1][j] != "" else crypto_func(i + 1, j)


def decrypto_func(i, j):
    if i == 0:
        return matrix[-1][j] if matrix[-1][j] != "" else decrypto_func(-1, j)
    else:
        return matrix[i - 1][j] if matrix[i - 1][j] != "" else decrypto_func(i - 1, j)


def find_idx_in_matrix(char, comp_fun):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == char:
                return comp_fun(i, j)

    return char


def crypto(source):
    result = ""

    for char in source:
        result += find_idx_in_matrix(char, crypto_func)

    return result


def decrypto(source):
    result = ""

    for char in source:
        result += find_idx_in_matrix(char, decrypto_func)

    return result


result = ""

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
