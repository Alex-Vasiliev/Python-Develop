# Створіть функцію, яка приймає рядок від користувача та записує його у файл.

file = open("Import_this.txt", 'r+')
string = input("Введіть текст який бажаете додати до файлу:\n")
file.read()
file.write(string)
file.seek(0)

print(file.read())
file.close()
