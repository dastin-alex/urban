# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# МОДУЛЬ 1. ДОПОЛНИТЕЛЬНОЕ ПРАКТИЧЕСКОЕ ЗАДАНИЕ (*)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Подсчёт среднего балла каждого ученика. На вход даны следующие данные.
# Список:
# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#
# Множество:
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке. Например,
#
# 'Aaron' - [5, 3, 3, 5, 4]
#
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением – его средний балл.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Программа :
# -*- coding: utf-8 -*-

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
tapline = list(students)
tapline.sort()
dico1 = {}
for i in range(5):
    exemplar = tapline[i]
    dico1[exemplar] = grades[i]
print(dico1)
dico2 = {}
for i in range(5):
    num = len(grades[i])
    total = sum(grades[i])
    exemplar = tapline[i]
    dico2[exemplar] = float(total/num)
print(dico2)

