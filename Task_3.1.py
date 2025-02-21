import os
os.system('cls')

print ("Регистрация на сайте...")

while True:
    login = input("Придумайте логин (минимум 3 символа): ")
    if len(login) < 3:
        print ("Логин должен содержать больше 3-х символов!")
    else: break

def validpass(password):
    return any(char.isupper() for char in password) \
    and any(char.islower() for char in password) \
    and any(char.isdigit() for char in password) \
    and any(not char.isalnum() for char in password)

while True:
    password = input("Придумайте надёжный пароль (минимум 8 символов): ")
    if len(password) < 8:
        print("Пароль должен содержать минимум 8 символов!")
    else:
        if not validpass(password):
            print ("Пароль должен содержать Заглавную и строчную букву, цифру и спец символ")
        else:
            checkpass = input("Повторите пароль, чтобы не возникло опечаток: ")
            if checkpass == password:
                print ("Регистрация завершена!")
                break
            else: print ("Пароли должны совпадать!")
        
