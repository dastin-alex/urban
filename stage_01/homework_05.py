# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# СЛОВАРИ И МНОЖЕСТВА. ДОМАШНЕЕ ЗАДАНИЕ
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 1)	создать переменную my_list и присвоить ей список из нескольких элементов, например, фруктов.
# 2)	вывести на экран список my_list;
# 3)	вывести на экран первый и последний элементы списка my_list;
# 4)	вывести на экран подсписок my_list с третьего до пятого элементов;
# 5)	изменить значение третьего элемента списка my_list;
# 6)	вывести на экран измененный список my_list;
# 7)	создать переменную my_dict и присвоить ей словарь с парами (ключ: значение), например, перевод некоторых слов;
# 8)	вывести на экран словарь my_dict;
# 9)	вывести на экран значение для заданного ключа в my_dict;
# 10)	изменить значение для заданного ключа или добавить новый в my_dict;
# 11)	вывести на экран измененный словарь my_dict.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Программа :
# -*- coding: utf-8 -*-

my_list = ['cucumber', 'cabbage', 'parsley', 'camomile', 'geranium', 'apple']
print('little things list  = ', my_list)
print('first elenent       = ', my_list[0])
print('last element        = ', my_list[-1])
print('3, 4, 5 indexes     = ', my_list[2:5])
my_list[2] = 'dandelion'
print('list with dandelion = ', my_list)
my_dict = {'cucumber': 'огурец',
           'cabbage': 'капуста',
           'parsley': 'петрушка',
           'camomile': 'ромашка',
           'geranium': 'герань',
           'apple': 'яблоко'}
print('vocabulaire         = ', my_dict)
print('my_dict [camomile]  = ', my_dict.get('camomile'))
my_dict['dandelion'] = 'одуванчик'
print('new vocabulaire     = ', my_dict)