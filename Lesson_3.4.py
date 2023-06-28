# Створіть клас Student для представлення студента. Додайте атрибути, такі як ім'я, прізвище і список оцінок.
# Реалізуйте метод __len__, який повертає кількість оцінок студента.
# Створіть список студентів і відсортуйте його за кількістю оцінок.

class Student:
    def __init__(self, first_name, last_name, grades):
        self.fname = first_name
        self.lname = last_name
        self.grades = grades

    def __len__(self):
        return len(self.grades)


al_do = [9, 9, 10, 11, 5, 4]
ju_ho = [11, 11, 11, 10, 9, 10, 8]
an_hu = [2, 4, 3, 5, 7, 7, 9, 10]
ju_vo = [5, 6, 5, 7, 8, 5, 9, 3, 6, 7, 5, 9, 10]
students = [
    Student("Alex", "Dorn", al_do),
    Student("Juli", "Horw", ju_ho),
    Student("Andgela", "Human", an_hu),
    Student("Julia", "Volbes", ju_vo)
]

sorted_students = sorted(students, key=lambda student: len(student))

for student in sorted_students:
    print(f"{student.fname} {student.lname}: {len(student)} оцінок")
