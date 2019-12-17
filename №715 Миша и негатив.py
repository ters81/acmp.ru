# ЗАДАЧА №715
# Миша и негатив
# https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=121&id_problem=749

# Миша уже научился хорошо фотографировать и недавно увлекся программированием.
# Первая программа, которую он написал, позволяет формировать негатив бинарного черно-белого изображения.
#
# Бинарное черно-белое изображение – это прямоугольник, состоящий из пикселей, каждый из которых может быть либо черным, либо белым.
# Негатив такого изображения получается путем замены каждого черного пикселя на белый, а каждого белого пикселя – на черный.
#
# Миша, как начинающий программист, написал свою программу с ошибкой, поэтому в результате ее исполнения мог получаться некорректный негатив.
# Для того чтобы оценить уровень несоответствия получаемого негатива исходному изображению, Миша начал тестировать свою программу.
#
# В качестве входных данных он использовал исходные изображения.
# Сформированные программой негативы он начал тщательно анализировать, каждый раз определяя число пикселей негатива, которые получены с ошибкой.
#
# Требуется написать программу, которая в качестве входных данных использует исходное бинарное черно-белое изображение и
# полученный Мишиной программой негатив, и на основе этого определяет количество пикселей, в которых допущена ошибка.
#
# Входные данные
# Первая строка входного файла INPUT.TXT содержит целые числа n и m (1 ≤ n, m ≤ 100) – высоту и ширину исходного изображения (в пикселях).
# Последующие n строк содержат описание исходного изображения. Каждая строка состоит из m символов «B» и «W».
# Символ «B» соответствует черному пикселю, а символ «W» – белому.
# Далее следует пустая строка, а после нее – описание выведенного Мишиной программой изображения в том же формате, что и исходное изображение.
#
# Выходные данные
# В выходной файл OUTPUT.TXT необходимо вывести число пикселей негатива, которые неправильно сформированы Мишиной программой.
#
# Примеры
# INPUT.TXT
# 3 4
# WBBW
# BBBB
# WBBW
#
# BWWW
# WWWB
# BWWB
# OUTPUT.TXT
# 2
# INPUT.TXT
# 2 2
# BW
# BB
#
# WW
# BW
# OUTPUT.TXT
# 2


n, m = map(int, input().split())

a = []
c = []
s = 0

for i in range(n):
    b = input()
    a.append(list(b))
input()
for i in range(n):
    b = input()
    c.append(list(b))

for i in range(n):
    for j in range(m):
        if a[i][j] == c[i][j]:
            s += 1

print(s)
