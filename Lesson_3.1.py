# Створіть клас Rectangle для представлення прямокутника. Додайте методи для обчислення площі та периметра прямокутника.
# Створіть об'єкт Rectangle і викличте ці методи.
# S = a · b - area
# Р = 2 · (а + b) - perimeter

class Rectangle:
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght

    def calculation_area(self):
        area = self.width * self.lenght
        print(f"Area: {area}")

    def calculation_perimeter(self):
        perimeter = 2*(self.width+self.lenght)
        print(f"Perimeter: {perimeter}")


in_width = int(input("Enter pleas width: "))
in_lenght = int(input("Enter pleas lenght: "))

rect1 = Rectangle(5, 8)
rect2 = Rectangle(in_width, in_lenght)

print("Rectangle 1\ncalculation area:")
rect1.calculation_area()
print("Rectangle 1\ncalculation perimeter:")
rect1.calculation_perimeter()
print("\nRectangle 2(input)\ncalculation area:")
rect2.calculation_area()
print("Rectangle 2(input)\ncalculation perimeter:")
rect2.calculation_perimeter()
