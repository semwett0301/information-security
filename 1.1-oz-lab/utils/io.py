import os
from enum import Enum

from termcolor import colored

from utils import alphabeds as a
from utils import utils as u

from tabulate import tabulate

import io


class Mode(Enum):
    CR = "cr"
    DEC = "dec"


def print_error(error):
    print(colored(error, 'red'))


def input_from_file():
    filename = str(input("Введите название файла, где хранится исходный текст (в директории test): "))

    file = io.open(os.path.abspath(os.curdir) + '\\1.1-oz-lab\\test\\' + filename, mode='r', encoding="utf-8")

    return file.read()


def input_matrix_from_file(alphabed):
    filename = str(input("Введите название файла, где хранится матрица (в директории src): "))

    matrix_rows = io.open(os.path.abspath(os.curdir) + '\\1.1-oz-lab\\src\\' + filename, mode='r',
                          encoding="utf-8").read().split('\n')
    matrix_size = u.count_matrix_size(alphabed)

    assert len(matrix_rows) == matrix_size, "Матрица некорректна"

    result = u.get_default_matrix(matrix_size)

    for i in range(matrix_size):
        result[i] = list(matrix_rows[i])

    return result


def input_alphabed():
    while True:
        alphabed = str(input("Выберите алфавит, в котором будет представлен текст (RU - русский, EN - английский): "))

        if alphabed == "RU":
            return a.RU

        if alphabed == "EN":
            return a.EN

        print_error("Некорректный алфавит")


def input_mode():
    while True:
        mode = str(input("Выберите режим работы (CR - зашифровать , DEC - дешифровать): "))

        if mode == "CR":
            return Mode.CR

        if mode == "DEC":
            return Mode.DEC

        print_error("Некорректный режим работы")


def input_matrix():
    while True:
        answer = str(input("Вы хотите использовать готовый квадрат Полибия (y - да , n - нет): "))

        if answer == "y":
            return True

        if answer == "n":
            return False

        print_error("Некорректный ответ")


def input_save_matrix():
    while True:
        answer = str(input("Вы хотите сохранить полученный квадрат Полибия? (y - да , n - нет): "))

        if answer == "y":
            return True

        if answer == "n":
            return False

        print_error("Некорректный ответ")


def print_result(result):
    print(colored("\nПолученный результат: " + result, 'green'))


def print_matrix(matrix):
    print("\nИспользуемый квадрат полибия:")
    print(colored(tabulate(matrix, tablefmt="grid", floatfmt="2.5f"), "green"))


def output_result(result):
    filename = str(input("Введите название файла, где где будет результат (в директории res): "))

    file = io.open(os.path.abspath(os.curdir) + '\\1.1-oz-lab\\res\\' + filename, mode='w',
                   encoding="utf-8")
    file.write(result)
    file.close()


def output_matrix(matrix):
    filename = str(input("Введите название файла, где где будет квадрат Полибия (в директории res): "))

    file = io.open(os.path.abspath(os.curdir) + '\\1.1-oz-lab\\res\\' + filename, mode='w',
                   encoding="utf-8")
    file.write(matrix)
    file.close()
