# Создайте любой список. Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран это значение.

import random

array = [0,0,0,0,0,0,0,0,0,0]

win = False
x = 0

for i in range (len(array)):
    array[i] = random.randint(0, 99)
    temp = array[i]
    if array.count(temp) > 1:
        win = True
        x = array[i]

if win == True:
    print ("Число повторяется. Это число: ", x, "\n Исходный массив: ", array)
else: print("Числа не повторяются. \n Исходный массив: ", array)