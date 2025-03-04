#Регистрация на сайте
import os
os.system('cls') #Чищу консоль каждый раз, чтобы не засорять

print ("Регистрация на сайте...")

while True: #Сделано чтобы регистрация начиналась заново автоматически
    login = input("Придумайте логин (минимум 3 символа): ")
    if len(login) < 3:
        print ("Логин должен содержать больше 3-х символов!")
    else: break #Если всё норм, то иду дальше

def validpass(password): #Создал функцию отдельно, чтобы не засорять код
    return any(char.isupper() for char in password) \
    and any(char.islower() for char in password) \
    and any(char.isdigit() for char in password) \
    and any(not char.isalnum() for char in password)
    #Тут я сначала проверил наличие букв верхнего и нижнего регистра, а затем цифр и спец символов
while True:
    password = input("Придумайте надёжный пароль (минимум 8 символов): ")
    if len(password) < 8: #Сначала проверяю длину пароля
        print("Пароль должен содержать минимум 8 символов!")
    else: #Затем проверяю его надёжность
        if not validpass(password):
            print ("Пароль должен содержать Заглавную и строчную букву, цифру и спец символ")
        else:
            checkpass = input("Повторите пароль, чтобы не возникло опечаток: ")
            if checkpass == password:
                print ("Регистрация завершена!")
                break #Завершаю программу
            else: print ("Пароли должны совпадать!") #Повторяю пока все условия не будут исполнены
        
