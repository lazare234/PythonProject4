import math

 #davaleba1
class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
    def __str__(self ):
        return f"{self.top}/{self.bottom}"
    def add(self, other):
        new_top = self.top * other.bottom + self.bottom * other.top
        new_bottom = self.bottom * other.bottom
        return Fraction(new_top, new_bottom)

    def inverse(self):
        return f"{self.bottom}/{self.top}"

fraction1 = Fraction(3, 5)
fraction2 = Fraction(7, 9)

fraction_sum = fraction1.add(fraction2)


print(f"Sum of {fraction1} and {fraction2} is {fraction_sum}")
print(f"Inverse of {fraction1} is {fraction1.inverse()}")

#davaleba2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_center(self):
        return math.sqrt(self.x**2 + self.y**2)

point1 = Point(3, 5)
point2 = Point(6, 9)

print(f"point1 distance from center is: {point1.distance_from_center()}")
print(f"point2 dintance from center is: {point2.distance_from_center()}")


#davaleba3


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

x1, y1 = map(int, input("შეიყვანეთ წერტილის a კოორდინატები (x1, y1): ").split())
x2, y2 = map(int, input("შეიყვანეთ წერტილის b კოორდინატები (x2, y2): ").split())

a = Point(x1, y1)
b = Point(x2, y2)

print(f"a წერტილი: {a}")
print(f"b წერტილი: {b}")

distance = a.distance(b)
print(f"მანძილი წერტილებს შორის: {distance}")





