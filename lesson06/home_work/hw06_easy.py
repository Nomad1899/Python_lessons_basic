# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt


class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @property
    def square(self):
        return 0.5 * abs((self._b[0] - self._a[0]) * (self._c[1] - self._a[1]) - (self._c[0] - self._a[0]) * (
                self._b[1] - self._a[1]))

    def long(self, x, y):
        return sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2)

    @property
    def perimeter(self):
        return self.long(self._a, self._b) + self.long(self._b, self._c) + self.long(self._a, self._c)

    @property
    def height(self):
        return [2 * self.square / self.long(self._a, self._b), 2 * self.square / self.long(self._a, self._c),
                2 * self.square / self.long(self._b, self._c)]


trin = Triangle([2, 10], [5, 4], [8, 3])
print(trin.square)
print (trin.long(trin._a, trin._b))
print (trin.perimeter)
print (trin.height)


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Isosceles_trapezium:
    def __init__(self, a, b, c, d):
        