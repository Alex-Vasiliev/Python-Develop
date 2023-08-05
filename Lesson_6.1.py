# Напишіть клас "Person", який має властивості name (ім'я) і age (вік).
# Зробіть ці властивості приватними, щоб вони не могли бути змінені напряму ззовні класу.
# Забезпечте методи для доступу до цих властивостей та встановлення їх значень.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __set_name(self, name):
        self.__name = name

    def __set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


person = Person("Alex", 21)
try:
    person._Person__set_name("John")
    person._Person__set_age(25)
    print(person.get_name()) # Виведе "John"
    print(person.get_age()) # Виведе 25
except AttributeError:
    print("Cannot access private method")
