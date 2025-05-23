class Restaurant:
    def __init__(self, name, type, rating):
        self.name = name
        self.type = type
        self.rating = rating
    
    def describe(self):
        print(f"Название: {self.name}, тип кухни: {self.type}")
    
    def open(self):
        print("Ресторан открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг изменён: {self.rating}")

Rest1 = Restaurant("Вкусно и точка", "фастфуд", 4.3)
Rest2 = Restaurant("Rostic's", "фастфуд", 4.5)
Rest3 = Restaurant("Burger King", "фастфуд", 4.6)

print(Rest1.name)
print(Rest1.type)
print(f"Рейтинг: {Rest1.rating}")
Rest1.describe()
Rest1.open()
Rest1.update_rating(5)

print(Rest2.name)
print(Rest2.type)
print(f"Рейтинг: {Rest2.rating}")
Rest2.describe()
Rest2.open()
Rest2.update_rating(5)

print(Rest3.name)
print(Rest3.type)
print(f"Рейтинг: {Rest3.rating}")
Rest3.describe()
Rest3.open()
Rest3.update_rating(5)