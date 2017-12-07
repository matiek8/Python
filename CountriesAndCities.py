"""
Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.

Формат ввода
Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны, затем идут названия городов этой страны. Название каждого город состоит из одного слова. В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.

Формат вывода
Для каждого из запроса выведите название страны, в котором находится данный город.

Тест 1
Входные данные:
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
3
Odessa
Moscow
Novgorod

Вывод программы:
Ukraine
Russia
Russia
"""

n = int(input())
stranaGorod = {}
for i in range(n):
    line1 = input()
    line = line1.split()
    strana = line[0].strip()
    gorods = line[1:]
    for gorod in gorods:
        if gorod not in stranaGorod:
            stranaGorod[gorod] = []
        stranaGorod[gorod].append(strana)
num = int(input())
otvet = {}
for j in range(num):
    town = input()
    if town in stranaGorod:
        country = stranaGorod[town]
        otvet[town] = []
    otvet[town].append(*country)
for town in otvet:
    print(' '.join(otvet[town]))
