from numpy.core.defchararray import isnumeric
from termcolor import colored

N = 573308195401

e_1 = 973169
e_2 = 550351

C_1 = '''
327707922480
455697659443
469317095774
41173012855
95114431187
183548202066
114278917224
111319924653
302320646938
497834611165
207393954597
469317095774
184588110993
'''

C_2 = '''
484439401392
92203619034
199299165882
100840467257
42877265767
537319004931
212469277565
335238563578
215934710265
248375790884
8143413999
199299165882
484325656679
'''

print(colored("Стартовые данные:", "green"))
print("C1: " + C_1)
print("C2: " + C_2)
print("N: " + str(N))
print("e1: " + str(e_1))
print("e2: " + str(e_2))


def get_int_list(source_list):
    result = []
    for curr_str in source_list.split():
        if isnumeric(curr_str):
            result.append(int(curr_str))
    return result


# Расширенный алгоритм Евклида
def extended_gcd(a, b):
    if a == 0:
        return 0, 1
    else:
        x_arg, y_arg = extended_gcd(b % a, a)
    return y_arg - (b // a) * x_arg, x_arg


C_1 = get_int_list(C_1)
C_2 = get_int_list(C_2)
result = ""

x, y = extended_gcd(e_1, e_2)

print(colored("\nПараметры, полученные расширенным алгоритмом Евклида", "green"))
print("r = " + str(x))
print("s = " + str(y))

print(colored("\nХод вычислений: ", "green"))

for i in range(len(C_1)):
    C_1_x = pow(C_1[i], x, N)
    C_2_y = pow(C_2[i], y, N)
    m = (C_1_x * C_2_y) % N
    current_result_bytes = int.to_bytes(m, length=4, byteorder='big')
    current_part = current_result_bytes.decode('windows-1251')
    result += current_part

    print("C1[", str(i), "]^r) mod N =", str(C_1_x))
    print("C2[", str(i), "]^s) mod N =", str(C_2_y))
    print("Полученная часть сообщения: ", str(current_part), "\n")

print(colored("RESULT = ", "green") + result)
