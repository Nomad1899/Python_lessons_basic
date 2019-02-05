# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
class Shcool:
    name = ''
    classrooms = []

    def __init__(self, name="Unnamded"):
        self.name = name
        self.classrooms = []

    def __str__(self):
        return f"Shcool {self.name}"

    def add_classroom(self, *classroooms):
        for i in classroooms
            self.classrooms.append(i)


class Classroom:
    number = 0
    liter = ''
    students = []
    teachers = []

    def __init__(self, number, classname: str):
        self.number, self.liter = classname[0], classname[1]
        self.students = []
        self.teachers = []

    def __str__(self):
        return f"Class {self.number}{self.liter}"

    def __repr__(self):
        return self.__str__()

    def add_students(self, student):
