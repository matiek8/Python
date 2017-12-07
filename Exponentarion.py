"""
Возводить в степень можно гораздо быстрее, чем за n умножений! Для этого нужно воспользоваться следующими рекуррентными соотношениями: aⁿ = (a²)ⁿ/² при четном n, aⁿ=a⋅aⁿ⁻¹ при нечетном n. Реализуйте алгоритм быстрого возведения в степень. Если вы все сделаете правильно,то сложность вашего алгоритма будет O(logn).

Формат ввода
Вводится действительное число a и целое число n.

Формат вывода
Выведите ответ на задачу.

"""

def power(a, n):
    if n % 2 == 0:
        if n == 0:
            return 1
        return (a ** 2) ** (n / 2)
    if n % 2 != 0:
        if n == 0:
            return 1
        return a * a ** (n - 1)


a = float(input())
n = float(input())
print(power(a, n))
