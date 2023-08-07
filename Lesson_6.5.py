# Розширте клас "Rectangle" з попереднього завдання, перевизначивши метод display_color().
# В методі display_color() виведіть повідомлення про колір прямокутника
# і додайте також виведення повідомлення про його розміри (ширину і висоту).

class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(self.color)


class Rectangles(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def display_color(self):
        super().display_color()
        print(" Color:", self.color, "\n", "Width:", self.width, "\n", "Height:", self.height)


rectangles = Rectangles("Blue", 10, 15)
rectangles.display_color()
