# -*- coding: utf-8 -*-

while 1 > 0:
    number = int(input("Введите число 1: "))
    if number % 2 == 0:
        print('число 1 чётное')
    else:
        print("число 1 нечётное")
        break
print('оператор после цикла')
while True:
    number = int(input("Введите число 2: "))
    if number % 2 == 0:
        print('число 2 чётное')
        continue
    else:
        print("число 2 нечётное")
    print('оператор внутри цикла')
    break
print('оператор после цикла')
