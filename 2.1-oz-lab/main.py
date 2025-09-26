import math

from termcolor import colored

source: str = '''
65044661056628
62698810905915
6384243931214
64581496145197
34821902367398
47317941132118
31834994240307
32916261351098
27399527764660
20797651714466
56226270748693
51223181240405'''

N: int = 70109121369029
e: int = 3401467

print(colored("Стартовые данные:", "green"))
print("Зашифрованная строка: " + source)
print("N: " + str(N))
print("e: " + str(e))

list_source = source.split()

A = int(math.floor(math.sqrt(N)) + 1)
i = 1

while True:
    current_A = A + i
    current_B = math.sqrt(current_A ** 2 - N)

    if int(current_B) == float(current_B):
        break

    i += 1

print(colored("\nПолученный аргумент А: ", "green") + str(current_A))
print(colored("Полученный аргумент B: ", "green") + str(current_B))


p = current_A + current_B
q = current_A - current_B

eilor = (p - 1) * (q - 1)
d = pow(e, -1, int(eilor))

result: str = ""

print(colored("\nИтоговые результаты:", "green"))
print("p: " + str(p))
print("q: " + str(q))
print("Функция Эйлера: " + str(eilor))
print("d: " + str(d))

print(colored("\nРасшифровка сообщения:", "green"))

for sym in list_source:
    dec_sym_int = pow(int(sym), d, N)
    dec_sym_bytes = int.to_bytes(dec_sym_int, length=4, byteorder='big')
    dec_sym = dec_sym_bytes.decode('windows-1251')
    print(sym + " -> " + str(dec_sym_int) + " -> " + dec_sym)
    result += dec_sym

print(colored("\nПолученное сообщение: ", "green") + result)
