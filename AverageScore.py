"""
В олимпиаде по информатике принимало участие несколько человек.
Определите и выведите средние баллы участников олимпиады в 9 классе, в 10 классе, в 11 классе.

Входные данные
Информация о результатах олимпиады записана в файле, каждая строка которого имеет вид:
фамилия имя класс балл.
Фамилия и имя — текстовые строки, не содержащие пробелов. Класс - одно из трех чисел 9, 10, 11. Балл - целое число от 0 до 100.
В этой задаче файл необходимо считывать построчно, не сохраняя содержимое файла в памяти целиком.

Выходные данные
Выведите три числа: средние баллы по 9 классу, по 10 классу, по 11 классу. Входной файл в кодировке utf-8 (используйте open('input.txt', 'r', encoding='utf-8')).

Тест 1
Входные данные:
Иванов Сергей 9 90
Сергеев Петр 10 91
Петров Василий 11 92
Васильев Иван 9 93

Вывод программы:
91.5 91.0 92.0
"""


inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
k9 = 0
k10 = 0
k11 = 0
c9 = 0
c10 = 0
c11 = 0
for line in lines:
    a = line.split()
    if int(a[2]) == 9:
        k9 = k9 + int(a[3])
        c9 = c9 + 1
    elif int(a[2]) == 10:
        k10 = k10 + int(a[3])
        c10 = c10 + 1
    else:
        k11 = k11 + int(a[3])
        c11 = c11 + 1
print(k9/c9, k10/c10, k11/c11)
inFile.close()
outFile.close()