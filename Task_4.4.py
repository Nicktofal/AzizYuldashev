#Смешание цветов
red = ("Красный")
green = ("Зелёный")
blue = ("Синий")

col1 = input("Введите название первого цвета: ")
col2 = input("Введите название второго цвета: ")

if col1.lower() == red.lower() or col2.lower() == red.lower() \
and col1.lower() == green.lower() or col2.lower() == green.lower(): print("Результат смешивания: Жёлтый", )
elif col1.lower() == green.lower() or col2 == green.lower() \
and col1.lower() == blue.lower() or col2.lower() == blue.lower(): print("Результат смешивания: Голубой", )
elif col1.lower() == blue.lower() or col2.lower() == blue.lower() \
and col1.lower() == red.lower() or col2.lower() == red.lower(): print("Результат смешивания: Фиолетовый", )
else: print("Вы можете выбрать только из 3-х основных цветов: красный, зелёный и синий")