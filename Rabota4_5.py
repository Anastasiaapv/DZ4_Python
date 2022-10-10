# Задача 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0


firstEquation  = ''
with open('C:/Users/79516/Documents/Анастасия/Обучение/Питон/Python/Lesson1/text005.txt', 'r') as data:
    firstEquation = data.read().split(' ')
    data.close()
sekondEquation  = ''
with open('C:/Users/79516/Documents/Анастасия/Обучение/Питон/Python/Lesson1/text006.txt', 'r') as data:
    sekondEquation = data.read().split(' ')
    data.close()

def readEquation():
    eqation = {}
    firstEquation = firstEquation.replace(" + ", " +").replace(" - ", " -").split()[:-2]
    for i in range(len(firstEquation)):
        firstEquation[i] = firstEquation[i].replace("+", "").split("x^")
        eqation[int(firstEquation[i][1])] = int(firstEquation[i][0])

    return eqation

def readEquation2():
    eqation = {}
    sekondEquation = sekondEquation.replace(" + ", " +").replace(" - ", " -").split()[:-2]
    for i in range(len(sekondEquation)):
        sekondEquation[i] = sekondEquation[i].replace("+", "").split("x^")
        eqation[int(sekondEquation[i][1])] = int(firstEquation[i][0])

    return eqation

finalList = {}
lList1 = readEquation()
lList2 = readEquation2()
print (lList1)
print (lList2)
for i in range(max(len(lList1), len(lList2)), -1, -1):
    first = lList1.get(i)
    second = lList2.get(i)
    if first != None or second != None:
        finalList[i] = (first if first != None else 0) + (second if second != None else 0)

print(finalList)

with open('text007.txt', 'w') as data:
    list_mn = 0
    data.write(" + ".join(map(str, list_mn)) + " = 0")
    print('Третий файл записан')

    