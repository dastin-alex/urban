# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# СПИСКИ И КОРТЕЖИ. ДОМАШНЕЕ ЗАДАНИЕ
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 1)	создать переменную immutable_var и присвоить ей кортеж из нескольких элементов разных типов данных;
# 2)	вывести элементы кортежа immutable_var на экран;
# 3)	попробовать изменить элементы кортежа immutable_var; объяснить почему нельзя это сделать;
# 4)	создать переменную mutable_list и присвоить ей список из нескольких элемен-тов;
# 5)	изменить элементы списка mutable_list;
# 6)	вывести на экран изменения списка mutable_list.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Программа :
# -*- coding: utf-8 -*-

immutable_var = 'tupel', False, 3.5, 0, [1, 2]
print('tulip     =', immutable_var)
mutable_list = [1, 2]
print('list      =', mutable_list)
mutable_list[0] = 3
mutable_list[1] = 4
print('new list  =', mutable_list)
immutable_var = immutable_var + tuple(mutable_list)
print('new tulip =', immutable_var)
