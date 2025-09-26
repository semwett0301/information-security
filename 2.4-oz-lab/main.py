from decimal import Decimal

from numpy.core.defchararray import isnumeric
from termcolor import colored

N_1 = 494980336813

N_2 = 495019868347

N_3 = 496510218943

C_1 = '''
405186643929
264588538265
58896941920
424470122024
445830333875
98276685134
210238595626
176058872641
185715938214
418034348683
52552730024
481876348312
438600466605
'''

C_2 = '''
298462743436
26894204289
266800308083
469634672912
423565503334
418775305332
112405305103
302129659337
323850375295
438598232992
10359943018
298111389169
277384894755
'''

C_3 = '''
372083067441
354383414943
31782553847
213067042090
22742161466
313919341914
71514328634
117790204322
268549130622
409153352258
316714994539
270152277750
128472385009
'''


def get_int_list(source_list):
    result = []
    for curr_str in source_list.split():
        if isnumeric(curr_str):
            result.append(int(curr_str))
    return result


print(colored("Стартовые данные:", "green"))
print("C1: " + C_1)
print("C2: " + C_2)
print("C3: " + C_3)
print("N1: " + str(N_1))
print("N2: " + str(N_2))
print("N3: " + str(N_3), "\n")

C_1 = get_int_list(C_1)
C_2 = get_int_list(C_2)
C_3 = get_int_list(C_3)

result = ""

M_0 = N_1 * N_2 * N_3

m_1 = N_2 * N_3
m_2 = N_1 * N_3
m_3 = N_1 * N_2

n_1 = pow(m_1, -1, N_1)
n_2 = pow(m_2, -1, N_2)
n_3 = pow(m_3, -1, N_3)

print(colored("Промежуточные вычисления", "green"))
print("M0: " + str(M_0))
print("m1: " + str(m_1))
print("m2: " + str(m_2))
print("m3: " + str(m_3))
print("n1: " + str(n_1))
print("n2: " + str(n_2))
print("n3: " + str(n_3), "\n")

for i in range(len(C_1)):
    y = C_1[i] * n_1 * m_1 + C_2[i] * n_2 * m_2 + C_3[i] * n_3 * m_3
    print("y[" + str(i) + "]: " + str(y))

    current_bytes = y % M_0
    print("y[" + str(i) + "] mod M0: " + str(current_bytes))

    current_result = round(current_bytes ** (Decimal(1 / 3)))
    print("y[" + str(i) + "] mod M0 ** (1 / 3): " + str(current_result))

    current_part = current_result.to_bytes(length=4, byteorder='big').decode('cp1251')
    print("Текущий текст: " + current_part, "\n")

    result += current_part

print(colored("Полученное сообщение: ", "green"))
print(result)
