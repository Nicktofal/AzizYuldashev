class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def describe(self):
        print(f"Название: {self.name}, тип кухни: {self.type}")
    
    def open(self):
        print("Ресторан открыт!")

newRestaurant = Restaurant("Вкусно и точка", "фастфуд")

print(newRestaurant.name)
print(newRestaurant.type)

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()