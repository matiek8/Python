"""
Дана последовательность натуральных чисел x₁ x₂ ..., xn.Стандартным отклонением называется величина
σ=sqrt(((((x₁-s)²+(x₂-s)²+…+(xn-s)²) / (n-1))))
где s = ((x₁+x₂+…+xn) / n) — среднее арифметическое последовательности, а sqrt - квадартный корень. Определите стандартное отклонение для данной последовательности натуральных чисел,завершающейся числом 0.

Формат ввода
Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит, а служит как признак ее окончания).

Формат вывода
Выведите ответ на задачу.
"""

import math

i = 0
a = []
n = 1
s = 0
q = 0
while n != 0:
    n = int(input())
    s = s + n
    if n == 0:
        break
    a.append(n)
d = len(a)
sum1 = 0
while i < len(a):
    sum1 = sum1 + (a[i] - s / d) ** 2
    i = i + 1
sq = math.sqrt(sum1/(d-1))
print(sq)