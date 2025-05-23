class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
    
    def describe_restaurant(self):
        print(f"Название: {self.restaurant_name}, тип кухни: {self.cuisine_type}")
    
    def open_restaurant(self):
        print("Ресторан открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг изменён: {self.rating}")

Rest1 = Restaurant("Вкусно и точка", "фастфуд", 4.3)
Rest2 = Restaurant("Rostic's", "фастфуд", 4.5)
Rest3 = Restaurant("Burger King", "фастфуд", 4.6)

print(Rest1.restaurant_name)
print(Rest1.cuisine_type)
print(f"Рейтинг: {Rest1.rating}")
Rest1.describe_restaurant()
Rest1.open_restaurant()
Rest1.update_rating(5)

print(Rest2.restaurant_name)
print(Rest2.cuisine_type)
print(f"Рейтинг: {Rest2.rating}")
Rest2.describe_restaurant()
Rest2.open_restaurant()
Rest2.update_rating(5)

print(Rest3.restaurant_name)
print(Rest3.cuisine_type)
print(f"Рейтинг: {Rest3.rating}")
Rest3.describe_restaurant()
Rest3.open_restaurant()
Rest3.update_rating(5)