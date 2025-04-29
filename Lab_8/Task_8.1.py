countries = {"Russia":"Moscow", "Japan":"Tokyo", "China":"Beijing"}

for key, value in sorted(countries.items()):
    print (key, " - ", value)


city = input("Введите название города: ")

for key, value in countries.items():
    if city == value:
        print(city, "является cтолицей", key)