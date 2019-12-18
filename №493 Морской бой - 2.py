# ЗАДАЧА №493
# Морской бой - 2
# https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=121&id_problem=750

# «Морской бой» - игра для двух участников, в которой игроки по очереди называют координаты на неизвестной им карте соперника.
# Если у соперника по этим координатам имеется корабль, то корабль или его часть «топится», а попавший получает право сделать еще один ход.
# Цель игрока - первым поразить все корабли противника.
#
# «Морской бой» очень популярен среди учеников одной физико-математической школы. Ребята очень любят в него играть на переменах.
# Вот и сейчас ученики Иннокентий и Емельян начали новую партию.
#
# Правила, по которым ребята расставляют корабли перед началом партии, несколько отличаются от классических.
# Во-первых, игра происходит на поле размером N×M, а не 10×10. Во-вторых, число кораблей, их размер и форма выбираются ребятами перед партией - так играть намного интереснее.
#
# Емельян уже расставил все свои корабли, кроме одного однопалубного. Такой корабль занимает ровно одну клетку.
#
# Задана расстановка кораблей Емельяна. Найдите число способов поставить оставшийся однопалубный корабль.
# При этом учитывайте, что по правилам его можно ставить только в ту клетку, все соседние с которой не заняты. В этой задаче соседними считаются клетки, имеющие общую сторону.
#
# Входные данные
# Первая строка входного файла INPUT.TXT содержит два числа: N и M (1 ≤ N, M ≤ 100).
# Последующие N строк описывают игровое поле - каждая из них содержит M символов. Символом «.» (точка) обозначена свободная клетка, символом «*» (звездочка) - занятая кораблем.
#
# Выходные данные
# В выходной файл OUTPUT.TXT выведите ответ на задачу.
#
# Примеры
# INPUT.TXT
# 4 4
# ****
# **..
# *...
# *...
# OUTPUT.TXT
# 4
# INPUT.TXT
# 4 3
# ***
# ...
# ...
# ***
# OUTPUT.TXT
# 0


n, m = map(int, input().split())

a = []
s = 0

a.append(list('.'*(m+2)))

for i in range(n):
    b = input()
    b = b.rjust((m+1), '.')
    b = b.ljust((m+2), '.')
    a.append(list(b))

a.append(list('.'*(m+2)))

for i in range(n):
    i += 1
    for j in range(m):
        j += 1
        if a[i-1][j] != '*' and a[i+1][j] != '*' and a[i][j-1] != '*' and a[i][j+1] != '*' and a[i][j] != '*':
            s += 1

print(s)
