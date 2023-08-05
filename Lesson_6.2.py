# Розширте клас "Person" з попереднього завдання, додавши методи для зміни значень імені та віку.
# Зробіть так, щоб ім'я не могло містити цифр, а вік був обмежений в діапазоні від 0 до 120.
# При спробі встановити недійсне значення, виведіть повідомлення про помилку.
import re


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __set_name(self, name):
        if re.findall(r"^[a-zA-Z ]+$", name):
            self.__name = name
        else:
            print("Error enter name")

    def __set_age(self, age):
        if re.match(r'^\d+$', age):
            age_value = int(age)
            if 0 <= age_value <= 120:
                self.__age = age
            else:
                print("Error enter age. 0-120")
        else:
            print("Error enter age. 0-120")

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


person = Person("Alex", 22)
person._Person__set_name("Jhon")
person._Person__set_age(str(22))
print(person.get_name(), person.get_age())


person._Person__set_name(str(22))
person._Person__set_age("Jhon")
# print(person.get_name(), person.get_age())
