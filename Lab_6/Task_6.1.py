# Напишите функцию, которая проверяет, делится ли введенное число на 3, или нет.

v = int(input("Введите число: "))

def func():
    if v % 3 == 0: 
        print ("Число делится на 3")
    else: print ("Число не делится на 3")

func()