# Створіть базовий клас "Shape" (фігура),
# який має властивість color (колір) і метод display_color() для виведення коліру фігури.
# Створіть похідний клас "Rectangle" (прямокутник),
# який наслідує властивість color і додає властивості width (ширина) і height (висота).
# Забезпечте можливість встановлення значень ширини і висоти прямокутника та виведення їх значень.

class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print("Color:", self.color)


class Rectangles(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


shape = Shape("Red")
shape.display_color()

rectangles = Rectangles("Blue", 10, 5)
rectangles.display_color()
print("Width -", rectangles.width)
print("Hight -", rectangles.height)
