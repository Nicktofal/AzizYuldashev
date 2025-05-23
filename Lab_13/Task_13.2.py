class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def describe(self):
        print(f"Название: {self.name}, тип кухни: {self.type}")
    
    def open(self):
        print("Ресторан открыт!")

Rest1 = Restaurant("Вкусно и точка", "фастфуд")
Rest2 = Restaurant("Rostic's", "фастфуд")
Rest3 = Restaurant("Burger King", "фастфуд")

print(Rest1.name)
print(Rest1.type)
Rest1.describe()
Rest1.open()

print(Rest2.name)
print(Rest2.type)
Rest2.describe()
Rest2.open()

print(Rest3.name)
print(Rest3.type)
Rest3.describe()
Rest3.open()