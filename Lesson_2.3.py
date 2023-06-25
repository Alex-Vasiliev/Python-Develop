# Напишіть програму, яка відкриває файл для читання та обробляє помилку FileNotFoundError, якщо файл не знайдено.

try:
    file = open("Files.txt")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Ваш файл не знайденно")


