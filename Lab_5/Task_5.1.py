# С клавиатуры вводятся поочередно N слов.  Напишите программу, которая соединяет эти слова в одну длинную строку, разделяя слова пробелами.

words_count = int(input("Введите количество слов: "))

String = ""

for i in range(words_count):
    word = input("Введите одно слово: ")
    String += word + " "

print(String)