# Напишіть клас "Person", який має властивості name (ім'я) і age (вік).
# Зробіть ці властивості приватними, щоб вони не могли бути змінені напряму ззовні класу.
# Забезпечте методи для доступу до цих властивостей та встановлення їх значень.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def _set_name(self, name):
        self._name = name

    def _set_age(self, age):
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


person = Person("Alex", 21)
try:
    person._set_name("John")
    person._set_age(25)
    print(person.get_name())
    print(person.get_age())
except AttributeError:
    print("Cannot access private method")
