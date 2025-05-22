from PIL import Image

holidays = {
    "Новый год": "new_year.jpg",
    "8 марта": "womens_day.jpg",
    "23 февраля": "mens_day.jpg",
    "День рождения": "birthday.jpg"
    }

print("Доступные праздники:", ", ".join(holidays.keys()))
holiday = input("К какому празднику нужна открытка? ")

if holiday in holidays:
    img = Image.open(holidays[holiday])
    img.show()
else:
    print("Такого праздника нет в списке")