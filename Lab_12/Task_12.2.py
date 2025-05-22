import json

with open('products.json', encoding='utf-8') as f:
    data = json.load(f)


data['products'].append({
    'name': input('Название: '),
    'price': int(input('Цена: ')),
    'available': input('В наличии (да/нет): ') == 'да',
    'weight': int(input('Вес: '))
})

# Записываем обратно
with open('products.json', 'w') as f:
    json.dump(data, f, indent=2)

for product in data['products']:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    print("В наличии" if product['available'] else "Нет в наличии")
    print()