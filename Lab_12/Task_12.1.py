import json

with open('products.json', encoding='utf-8') as f:
    data = json.load(f)

for product in data['products']:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    print("В наличии" if product['available'] else "Нет в наличии")