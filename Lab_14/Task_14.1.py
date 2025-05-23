class Restaurant:
    def __init__(self, name, type, rating=0):
        self.name = name
        self.type = type
        self.rating = rating

class IceCreamStand(Restaurant):
    def __init__(self, name, type, flavors):
        super().__init__(name, type)
        self.flavors = flavors
    
    def show_flavors(self):
        print("Сорта мороженого:", ", ".join(self.flavors))

ice_cream = IceCreamStand("Cold Stone", "кафе-мороженое", ["ваниль", "шоколад", "клубника"])

print(ice_cream.name)
print(ice_cream.type)
ice_cream.show_flavors()