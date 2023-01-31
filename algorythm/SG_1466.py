class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        return None


class Rectangle:
    p1 = 0
    p2 = 0
    w = 0
    l = 0

    @classmethod
    def __init__(cls, cl1, cl2):
        cls.p1 = (cl1.x, cl1.y)
        cls.p2 = (cl2.x, cl2.y)
        cls.w = max(cls.p1[0], cls.p2[0]) - min(cls.p1[0], cls.p2[0])
        cls.l = max(cls.p1[1], cls.p2[1]) - min(cls.p1[1], cls.p2[1])

    @classmethod
    def get_area(cls):
        return cls.w * cls.l

    @classmethod
    def get_perimeter(cls):
        return 2 * (cls.w + cls.l)

    @classmethod
    def is_square(cls):
        return cls.w == cls.l


p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)

print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())