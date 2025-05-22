total = 0

print("Нужно купить:")
with open("list.csv", encoding="utf-8") as f:
    next(f)  # Пропускаем заголовок
    for line in f:
        product, amount, price = line.strip().split(',')
        total += int(amount) * int(price)
        print(f"{product} - {amount} шт. за {price} руб.")
print(f"Итоговая сумма: {total} руб.")