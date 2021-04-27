class Rectangle:

    # When a Rectangle object is created, it should be initialized with width and height attributes.
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    # set the width based on the passed argument
    def set_width(self, width):
        self.width = width

    # set the height based on the passed argument
    def set_height(self, height):
        self.height = height

    # Returns area (width * height)
    def get_area(self):
        return (self.width * self.height)

    # Returns perimeter (2 * width + 2 * height)
    def get_perimeter(self):
        return (2 * self.width + 2* self.height)

class Square(Rectangle):
    pass
