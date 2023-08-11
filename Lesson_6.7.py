class Rectangle:
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

    def display_color(self):
        print("Color:", self.color)


class Square(Rectangle):
    def __init__(self, color, side_length):
        super().__init__(color, side_length, side_length)
        self.color = color
        self.side_length = side_length

    def display_color(self):
        print("Color:", self.color)

    def width(self):
        return self.side_length

    def height(self):
        return self.side_length


square = Square("Green", 8)
square.display_color()
print(square.width)
print(square.height)
print(square.side_length)
