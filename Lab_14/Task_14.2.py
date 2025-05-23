class Restaurant:
    def __init__(self, name, type, rating=0):
        self.name = name
        self.type = type
        self.rating = rating

class IceCreamStand(Restaurant):
    def __init__(self, name, type, flavors, location, working_hours):
        super().__init__(name, type)
        self.flavors = flavors
        self.location = location
        self.working_hours = working_hours
        self.ice_types = {
            'на палочке': [],
            'мягкое': [],
            'фруктовый лёд': []
        }
    
    def show_flavors(self):
        print("Доступные сорта:", ", ".join(self.flavors))
    
    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print(f"Добавлен новый сорт: {flavor}")
    
    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Сорт {flavor} удалён")
        else:
            print(f"Сорта {flavor} нет в списке")
    
    def has_flavor(self, flavor):
        return flavor in self.flavors
    
    def add_ice_type(self, ice_type, flavors):
        if ice_type in self.ice_types:
            self.ice_types[ice_type].extend(flavors)
            print(f"Добавлены сорта {flavors} для типа '{ice_type}'")
    
    def show_ice_types(self):
        for ice_type, flavors in self.ice_types.items():
            print(f"{ice_type}: {', '.join(flavors) if flavors else 'нет сортов'}")
        

ice_shop = IceCreamStand(
    name="Морожко",
    type="кафе-мороженое",
    flavors=["ваниль", "шоколад", "клубника"],
    location="ТЦ 'Атриум'",
    working_hours="10:00-22:00"
)

print(ice_shop.name)
print(ice_shop.type)
ice_shop.show_flavors()

ice_shop.add_flavor("банан")
ice_shop.remove_flavor("клубника")
print("Есть ли манго?", ice_shop.has_flavor("манго"))

ice_shop.add_ice_type("на палочке", ["шоколад", "ваниль"])
ice_shop.add_ice_type("мягкое", ["банан", "крем-брюле"])

print("Информация о кафе:")
print(f"Локация: {ice_shop.location}")
print(f"Часы работы: {ice_shop.working_hours}\n")

ice_shop.show_flavors()
print("Типы мороженого:")
ice_shop.show_ice_types()