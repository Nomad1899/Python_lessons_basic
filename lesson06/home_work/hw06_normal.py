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

class Person:
    def __init__(self,last_name, first_name, second_name):
        self.last_name = last_name
        self.first_name = first_name
        self.second_name = second_name

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.second_name}'

class Parent(Person):
    def __init__(self, last_name, first_name, second_name):
        super().__init__(last_name, first_name, second_name)
        self.children = []


class Student(Person):
    def __init__(self, last_name, first_name, second_name, mother: Parent, father: Parent):
        super().__init__(last_name, first_name, second_name)
        self.class_group = None
        self.mother = mother
        self.father = father
        mother.children.append(self)
        father.children.append(self)

    def set_class_group(self, class_group):
        self.class_group = class_group
