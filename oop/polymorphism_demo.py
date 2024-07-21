import math


class Shape:
    def area(slef):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


def main():
    shapes = [Rectangle(10, 5), Circle(7)]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


if __name__ == "__main__":
    main()
