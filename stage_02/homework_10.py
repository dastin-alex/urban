# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ФУНКЦИИ. ДОМАШНЕЕ ЗАДАНИЕ
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 1)	создать функцию def print_params, которая в своем теле два раза будет распе-чатывать переданное значение из параметра;
# 2)	несколько раз вызвать функцию print_params;
# 3)	запустить поэтапное выполнение программы, использовать нажатие иконки «жу-чок» справа от запуска проекта;
# 4)	для перехода к следующему шагу выполнения программы использовать кнопку «Step Over»;
# 5)	наблюдать в консоли результат работы программы.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Программа :
# -*- coding: utf-8 -*-


def print_params(param1, count):
    for i in range(count):
        print(param1)


print_params('hello', 2)
print_params('>>>', 5)
print_params("that is all talks", 2)
