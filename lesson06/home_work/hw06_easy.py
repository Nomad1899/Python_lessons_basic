# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
import math


class Point:
    x, y = 0, 0

    def __init__(self, x: int, y: int):
        self.x, self, y = x, y

    def __str__(self):
        return str([self.x, self.y])


class Side:
    a, b = None, None

    def __init__(self, a: Point, b: Point):
        self.a, self.b = a, b

    def __str__(self):
        return f"Side: {self.a}->{self.b}"

    @property
    def length(self):
        if self.a is not None and self.b is not None:
            vector = Point(self.b.x - self.a.x, self.b.y - self.a.y)
            value = math.sqrt((vector.x ** 2) + (vector.y ** 2))
            return round(value, 2)
        else:
            return 0


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.a, self.b, self.c = a, b, c

    @property
    def ab(self):
        return Side(self.a, self.b).length

    @property
    def bc(self):
        return Side(self.b, self.c).length

    @property
    def ca(self):
        return Side(self.c, self.a).length

    def perimeter(self, full=True):
        p = round(self.ab + self.bc + self.ca, 5)
        return p if full else p / 2

    def area(self):
        p = self.perimeter(False)
        s = math.sqrt(p * (p - self.ab) * (p - self.bc) * (p - self.ca))
        return round(s, 5)

    def height(self):
        p = self.perimeter(False)
        h = (2 * self.area()) / self.ab
        return round(h, 3)
class Trapeze:
    def __init__(self,a:Point, b: Point, c:Point, d:Point):
        self.a,self.b,self.c,self.d=a,b,c,d

    def __str__(self):
        return f"Trapeze {self.a}, {self.b},{self.c},{self.d}"
    @property
    def ab(self):
        return Side(self.a,self.b).length
    @property
    def bc(self):
        return Side(self.b,self.c).length
    @property
    def cd(self):
        return Side(self.b,self.c).length
    @property
    def da(self):
        return Side(self.d,self.a).length
    def perimeter(self):
        p=round(self.ab+self.bc+self.cd+self.da,5)
