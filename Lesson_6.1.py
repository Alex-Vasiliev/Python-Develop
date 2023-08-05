# Напишіть клас "Person", який має властивості name (ім'я) і age (вік).
# Зробіть ці властивості приватними, щоб вони не могли бути змінені напряму ззовні класу.
# Забезпечте методи для доступу до цих властивостей та встановлення їх значень.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __set_name(self):
        return self.__name

    def __set_age(self):
        return self.__age


person = Person("Alex", 21)

# з помилкою
try:
    print(person.__set_name(), person.__set_age())
except AttributeError:
    print("Cannot access private method")

# в обхід приватності
try:
    print(person._Person__set_name())
except AttributeError:
    print("Cannot access private method")
