# Создайте два списка: один из 10 фамилий студентов Вашей группы, другой из 10 фамилий студентов другой группы.

import random

Group1 = ["Петров", "Сидоров", "Иванов", "Кузнецов", "Смирнов", 
            "Васильев", "Попов", "Новиков", "Федоров", "Морозов"]
Group2 = ["Лебедев", "Соловьев", "Волков", "Козлов", "Егоров",
               "Орлов", "Андреев", "Макаров", "Николаев", "Захаров"]

# a)
team = []
while len(team) < 5:
    student = random.choice(Group1)
    if student not in team:
        team.append(student)

while len(team) < 10:
    student = random.choice(Group2)
    if student not in team:
        team.append(student)

team = tuple(team)  # Преобразуем список в кортеж

# b)
print("Моя группа:", Group1)
print("Другая группа:", Group2)

# c)
print("Количество человек в команде:", len(team))

# d)
sort = list(team)
sort.sort()
sort = tuple(sort)
print("Отсортированная команда:", sort)

# e)
if "Иванов" in team:
    count = team.count("Иванов")
    print("Иванов есть в команде. Количество:", count)
else:
    print("Иванова нет в команде")