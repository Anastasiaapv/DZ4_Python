# Задача 3. Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

newLst = {}
finalStr = ''
lstStr = list(map(str, input('Задайте последовательность чисел: ')))
print(f"Исходный список: {lstStr}")

for c in lstStr:
    if newLst.get(c):
        newLst[c] = newLst.get(c)+1
    else:
        newLst[c]=1

for i in newLst.items():
    if i[1]==1:
        finalStr +=str(i[0])
print(f'Список из неповторяющихся элементов: {finalStr}') if finalStr else print ('Неповторяющихся позиций нет')