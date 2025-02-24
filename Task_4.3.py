#Определение високосности года
while True:
    year = int(input("Введите год: "))
    if not year % 100 == 0 and year % 4 == 0 or year % 400 == 0:
        print (f"Год", year, "високосный")
    else:
        print (f"Год", year, "не високосный")