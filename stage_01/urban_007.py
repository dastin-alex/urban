# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 1.11 СЛОВАРИ И МНОЖЕСТВА
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# В WEB-разработке часто применяются словари и множества. В словаре элементы хранятся парами {ключ: значение}. Для вы-
# деления словаря используются фигурные скобки. Элементы множества также перечисляются в фигурных скобках {1, 2, 3}.
# Элементы множества указываются как в списках, однако, это не одно и то же. Элементы множества, в отличие от списка,
# уникальные. Список с помощью функции set () можно преобразовать в множество. По-французски dico – это словарь,
# ensemble – множество.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Программа :

# -*- coding: utf-8 -*-

phone_book = {'Denis': 8800, 'Max': 8801}
print(phone_book)
print(phone_book['Denis'])
phone_book['Denis'] = 8888
print(phone_book)
phone_book['Anton'] = 8802
print(phone_book)
del phone_book['Max']
print(phone_book)
phone_book.update({'Alex': 8803, 'Semen': 8804})
print(phone_book)
print(phone_book.items())
print(phone_book.keys())
print(phone_book.values())
print(phone_book.get('Alex'))
print(phone_book.get('Olga'))
print(phone_book.get('Olga', 'Такого ключа нет'))
print(phone_book)
a = phone_book.pop('Anton')
print(a)
print(phone_book)
tableau = [1, 2, 3, 1, 1, 2]
print(tableau)
tableau.pop(1)
print(tableau)
phone_book['Denis'] = [8800, 8888]
print(phone_book)
ensemble = {1, 2, 3, 1, 1, 2, True, (1, 0)}
print(ensemble)
print(tableau)
print(set(tableau))
ensemble = set(tableau)
print(ensemble)
print(ensemble.discard(1))
print(ensemble)
print(ensemble.remove(2))
print(ensemble)
print(ensemble.add(5))
print(ensemble)
dico = {}
dico['elephant'] = 'слон'
print(dico['elephant'])
dico['car'] = 'автомобиль'
print(dico)
dico[3.14] = "PI"
print(dico)
print('3.14' in dico)
print(3.14 in dico)
print("car" in dico)
print(dico.get('cat', 'elephant'))
ensemble_1 = set([1, 2, 3, 3, 2, 1])
print(ensemble_1)
ensemble_2 = set([0, 2, 4, 4, 2, 0])
print(ensemble_2)
print(ensemble_1 | ensemble_2)
print(ensemble_1 & ensemble_2)
