# Створіть клас Student, який представляє студента.
# Реалізуйте атрибут класу для відстеження кількості студентів.
# Для цього змінюйте значення атрибуту класу у методі __init__ .
# Та створіть клас метод для виведення загальної кількості студентів.


class Student:

    number_of_students = 0

    def __init__(self, name, year, group):
        self.last_name = name
        self.year = year
        self.group = group
        Student.number_of_students += 1

    @classmethod
    def global_number(cls):
        return f"total number of students: {cls.number_of_students}"


stud = Student("John", 2001, "GP-17 2/9")
stud2 = Student("Nikolas", 2002, "GP-17 2/9")
stud3 = Student("Sara", 2000, "GP-17 2/9")

print(Student.global_number())
