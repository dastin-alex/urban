# -*- coding: utf-8 -*-

food = ["apple", "coconut", "banana"]
print(food)
print(food[0])
food[0] = 'peach'
print(food)
food.append(True)
print(food)
food.extend('capital')
print(food)
food.extend(['capital', 2])
print(food)
food.remove('a')
print(food)
food.remove('a')
print(food)
print('a' in food)
print('a' not in food)
print(food[2:7])
print(food[::2])
print(food[:7:-1])
