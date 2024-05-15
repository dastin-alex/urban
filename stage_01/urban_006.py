# -*- coding: utf-8 -*-

tupel_1 = 1, 2, 3, 4
print(tupel_1)
tupel_2 = 1, 2, 3, 4
print(tupel_2)
tupel_3 = tuple([1, 2, 3, 4])
print(tupel_3)
print(type(tupel_1), type(tupel_2), type(tupel_3))
tupel = 1, 2, 3, 4, True, 'string'
print(tupel[0], tupel[4], tupel[5])
print(tupel)
tableau = [1, 2, 3, 4, True, 'string']
print(tableau)
print("list size  =", tableau.__sizeof__())
print("tulip size =", tupel.__sizeof__())
tupel_4 = (0, [1, 2], 3, 4)
print(tupel_4)
tupel_4[1][0] = 5
print(tupel_4)
tupel_4 = tupel_4 + ('capital', 7)
print(tupel_4)
tupel_5 = (1, 2) * 3
print(tupel_5)
