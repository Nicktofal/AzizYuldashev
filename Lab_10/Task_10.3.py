from PIL import Image, ImageDraw, ImageFont

cards = {
    "День рождения": "birthday.jpg",
    "Новый год": "new_year.jpg",
    "8 марта": "womens_day.jpg"
}

print("Доступные праздники:", ", ".join(cards.keys()))
holiday = input("Выберите праздник: ")
name = input("Введите имя для поздравления: ")

if holiday not in cards:
    print("Такого праздника нет в списке")
    exit()

img = Image.open(cards[holiday])
draw = ImageDraw.Draw(img)

# Настройки текста
text = name + ", congratulation!"
font = ImageFont.truetype("ARLRDBD.TTF", 40)
text_color = (255, 0, 0)  # Красный цвет

# Рассчитываем позицию текста (внизу по центру)
text_width = draw.textlength(text, font=font)
x = (img.width - text_width) / 2
y = img.height - 100  # Отступ от нижнего края

# Добавляем текст на изображение
draw.text((x, y), text, fill=text_color, font=font)

# Сохраняем и показываем результат
new_filename = f"congrats_{holiday.replace(' ', '_')}.png"
img.save(new_filename)
img.show()