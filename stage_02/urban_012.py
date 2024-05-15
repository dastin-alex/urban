# -*- coding: utf-8 -*-
for i in 1, 2, 3, 4:
    print("OK")
for i in 1, 2, 3, 4:
    print('i = ', i)
for i in 'hello':
    print(i)
tableau = ['one', 'two', 'three']
for i in tableau:
    print(i)
for i in tableau:
    if i == "three":
        tableau.remove(i)
print(tableau)
for i in range(5):
    print(i)
tableau = ['one', 'two', 'three']
print(tableau)
for i in range(len(tableau)):
    print(tableau[i])
    tableau[i] = 'мяу'
    print(tableau[i])
print(tableau)
tableau = [2, 7, 3, 4, 5]
sum1 = sum(tableau)
sum2 = 0
for i in range(len(tableau)):
    sum2 += tableau[i]
print('sum1 = ', sum1, 'sum2 = ', sum2)
for i in range(1, 11, 2):
    print(i)
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j}')
dico = {'a': 4, 'b': 5, 'c': 7}
for i in dico:
    print(i, dico[i])
for i, k in dico.items():
    print(i, k)
