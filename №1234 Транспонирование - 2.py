# ЗАДАЧА №1234
# Транспонирование - 2
# https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=120&id_problem=743

# Задана целочисленная квадратная матрица размером N x N. Требуется транспонировать ее относительно побочной диагонали.
#
# Входные данные
# Первая строка входного файла INPUT.TXT содержит натуральное число N – количество строк и столбцов матрицы. В каждой из последующих N строк записаны N целых чисел – элементы матрицы. Все числа во входных данных не превышают 100 по абсолютной величине.
#
# Выходные данные
# В выходной файл OUTPUT.TXT выведите матрицу, полученную транспонированием исходной матрицы относительно побочной диагонали.
#
# Пример
# №	INPUT.TXT
# 5
# 3 4 9 6 2
# 8 2 0 5 1
# 4 7 4 8 7
# 7 1 3 3 8
# 5 6 3 7 0
# OUTPUT.TXT
# 0 8 7 1 2
# 7 3 8 5 6
# 3 3 4 0 9
# 6 1 7 2 4
# 5 7 4 8 3

N = int(input())

a = []

for i in range(N):
    b = list(map(int, input().split()))
    a.append(b)

for i in range(N):
    i=N-i-1
    for j in range(N):
        j=N-j-1
        print(a[j][i], end=' ')
    print()
