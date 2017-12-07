"""
Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку. Слова должны быть отсортированы по убыванию их количества появления в тексте, а при одинаковой частоте появления — в лексикографическом порядке.

Указание.
После того, как вы создадите словарь всех слов, вам захочется отсортироватьего по частоте встречаемости слова. Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов: частота встречаемости словаи само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет сортировать список кортежей, при этом кортежи сравниваются по первому элементу, а если они равны —то по второму. Это почти то, что требуется в задаче.

Формат ввода
Вводится текст.

Формат вывода
Выведите ответ на задачу.

Тест 1
Входные данные:
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme

Вывод программы:
damme
is
name
van
bond
claude
hi
my
james
jean
what
your
"""

import operator
file = open('input.txt', 'r')
b = file.read()
a = ''
for line in b:
    line.split('\n')
    a = a + line
slovar = dict()
lst = a.split()
lst.sort()
for word in lst:
    if word not in slovar:
        slovar[word] = 0
    slovar[word] += 1
sl_it = slovar.items()
word_count_items = sorted(sl_it, key=operator.itemgetter(1), reverse=True)
for x in word_count_items:
    print(x[0])
