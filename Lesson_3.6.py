# Створіть клас Circle, який представляє коло. Реалізуйте методи для обчислення площі та довжини кола.
# Використовуйте аттрибут класу для зберігання значення π (pi).
# Length - l = 2 * π * r
#          l = π * d
# Area - S = π * r^2
#        S = (π/4) * d^2

class Circle:
    pi = 3.14159

    def __init__(self, diameter=0, radius=0):
        self.diameter = diameter
        self.radius = radius

    def area_calculation(self):
        if self.radius > 0:
            area = self.pi * self.radius ** 2
            print(f"Area:", area)

        elif self.diameter > 0:
            area = (self.pi/4) * self.diameter ** 2
            print(f"Area:", area)
        else:
            print("Error")

    def length_calculation(self):
        if self.diameter > 0:
            length = self.pi * self.diameter
            print("Length:", length)
        elif self.radius > 0:
            length = 2 * self.pi * self.radius
            print("Length:", length)
        else:
            return f"Error!"


calculation_method = int(input("Which method do you want to calculate length and area ?:\n"
                               "1 - Diametr\n"
                               "2 - Radius\n"))
if calculation_method == 1:
    user_inpD = int(input("Enter diameter circle: "))
    finish = Circle(user_inpD)
    finish.length_calculation()
    finish.area_calculation()

elif calculation_method == 2:
    user_inpR = int(input("Enter radius circle: "))
    finish = Circle(0, user_inpR)
    finish.length_calculation()
    finish.area_calculation()
else:
    print("Error!")

