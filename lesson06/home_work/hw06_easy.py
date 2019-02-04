# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt

class Vector:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f'( {self.start}; {self.end} )'

    def __get_legs(self):
        k1 = abs(self.start[0] - self.end[0])
        k2 = abs(self.start[1] - self.end[1])
        return k1, k2

    def get_length(self):
        k1, k2 = self.__get_legs()
        return (k1 ** 2 + k2 ** 2) ** (1 / 2)

    def get_point(self):
        return self.end[0] - self.start[0], self.end[1] - self.start[1]

    def get_matrix(self):
        return [[self.start[0], self.end[0]], [self.start[1], self.end[1]]]


class Shape:

    def __init__(self, points):
        """
        Base class shapes
        :param points: List of tuples with coord X, Y
        """
        count = len(points)
        self.vectors = []
        for i in range(count):
            self.vectors.append(Vector(points[i], points[((i + 1) % count)]))

    def get_square(self):
        vectors_det = []
        for v in self.vectors:
            m = v.get_matrix()
            vectors_det.append(m[0][0] * m[1][1] - m[0][1] * m[1][0])
        return abs(sum(vectors_det) / 2)

    def get_perimeter(self):
        return sum([v.get_length() for v in self.vectors]


class Triangle(Shape):

    def __init__(self, a, b, c):
        """
        Triangle class
        :param a: Tuple with coord X, Y
        :param b: Tuple with coord X, Y
        :param c: Tuple with coord X, Y
        """
        super().__init__([a, b, c])

    def get_triangle_square(self):
        pp = self.get_perimeter() / 2
        a = self.vectors[0].get_length()
        b = self.vectors[1].get_length()
        c = self.vectors[2].get_length()
        return (pp * (pp - a) * (pp - b) * (pp - c)) ** (1/2)

    def get_height(self, vector_num=0):
        return self.get_square() * 2 / self.vectors[vector_num].get_length()


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze(Shape):

    def __init__(self, a, b, c, d):
        """
        Trapeze class
        :param a: Tuple with coord X, Y
        :param b: Tuple with coord X, Y
        :param c: Tuple with coord X, Y
        :param d: Tuple with coord X, Y
        """
        super().__init__([a, b, c, d])

    def check_equilateral(self):

        def __check_equal_diagonal(vector1, vector2):
            d1 = Vector(vector1.start, vector2.start)
            d2 = Vector(vector1.end, vector2.end)
            return d1.get_length() == d2.get_length()

        if self.vectors[0].get_length() == self.vectors[2].get_length():
            return __check_equal_diagonal(self.vectors[0], self.vectors[2])
        elif self.vectors[1].get_length() == self.vectors[3].get_length():
            return __check_equal_diagonal(self.vectors[1], self.vectors[3])
        else:
            return False

    def get_length_of_sides(self):
        for i in range(len(self.vectors)):
            yield self.vectors[i].get_length()