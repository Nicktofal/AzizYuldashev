# Задан кортеж с перечнем названий дней недели. Спросить у пользователя, сколько выходных на неделе он хочет и вывести два списка:

days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')

print("Сколько выходных вы хотите? (от 1 до 7)")
count = int(input())

weekend = []
for i in range(count):
    weekend.append(days[6 - i])

work_days = []
for day in days:
    if day not in weekend:
        work_days.append(day)

print("Ваши выходные дни:", ", ".join(weekend))
print("Ваши рабочие дни:", ", ".join(work_days))