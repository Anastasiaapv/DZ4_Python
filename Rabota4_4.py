# Задача 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от-100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

import random
k = int(input("Введите натуральную степень многочлена: " ))
def write_file(st):
  with open('text004.txt', 'w') as data:
        data.write(st)
def rnd():
     return random.randint(0,9)

def create_mn(k):
    lstA = [rnd() for i in range(k+1)]
    return lstA
    
def create_str(sp):
    wr = ''
    lstA= sp[::-1]
    if len(lstA) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lstA)):
            if i != len(lstA) - 1 and lstA[i] != 0 and i != len(lstA) - 2:
                wr += f'{lstA[i]}x^{len(lstA)-i-1}'
                if lstA[i+1] != 0:
                    wr += ' + '
            elif i == len(lstA) - 2 and lstA[i] != 0:
                wr += f'{lstA[i]}x'
                if lstA[i+1] != 0:
                    wr += ' + '
            elif i == len(lstA) - 1 and lstA[i] != 0:
                wr += f'{lstA[i]} = 0'
            elif i == len(lstA) - 1 and lstA[i] == 0:
                wr += ' = 0'
    return wr

koef = create_mn(k)
write_file(create_str(koef))