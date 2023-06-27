# Створіть клас Rectangle для представлення прямокутника. Додайте методи для обчислення площі та периметра прямокутника.
# Створіть об'єкт Rectangle і викличте ці методи.
# S = a · b - area
# Р = 2 · (а + b) - perimeter

class Rectangle:
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght

    def calculation(self):
        area = self.width * self.lenght
        perimeter = 2*(self.width + self.lenght)
        print(f"Area: {area}\nPerimeter: {perimeter}")


in_width = int(input("Enter pleas width: "))
in_lenght = int(input("Enter pleas lenght: "))

rect1 = Rectangle(5, 8)
rect2 = Rectangle(10, 20)
rect3 = Rectangle(in_width, in_lenght)

print("Rectangle 1")
rect1.calculation()
print("\nRectangle 2")
rect2.calculation()
print("\nRectangle 3")
rect3.calculation()

