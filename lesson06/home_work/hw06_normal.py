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

import random
import string
import os
from typing import List


class Person:
    def __init__(self, last_name, first_name, second_name):
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


class Teacher(Person):
    def __init__(self, last_name, first_name, second_name, lesson_subject):
        super().__init__(last_name, first_name, second_name)
        self.lesson_subject = lesson_subject
        self.class_groups = []

    def __str__(self):
        return f'{super().__str__()} ({self.lesson_subject})'


class ClassGroup:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.lesson_teacher = {}

    def add_students(self, studs):
        for s in studs:
            self.add_student(s)

    def add_student(self, stud):
        stud.set_class_group(self)
        self.students.append(stud)

    def set_lesson_teacher(self, teacher: Teacher):
        self.lesson_teacher[teacher.lesson_subject] = teacher
        teacher.class_groups.append(self)

    def get_all_student_names(self):
        return [st.__str__() for st in self.students]

    def __str__(self):
        return f'{self.name} Students count: {len(self.students)}'


class School:
    def __init__(self):
        self.class_groups: List[ClassGroup] = []
        self.all_studs: List[Student] = []

    def get_all_classes_names(self):
        return [gr.name for gr in self.class_groups]

    def get_all_students(self):
        if len(self.all_studs) == 0:
            for gr in self.class_groups:
                for st in gr.students:
                    self.all_studs.append(st)
        return self.all_studs


# ======================================================= #


lessons = ['Алгебра', 'Геометрия', 'Русский язык', 'Литература', 'География', 'Биология']
names = {
    'f_last_names': [],
    'm_last_names': [],
    'f_first_names': [],
    'm_first_names': [],
    'f_second_names': [],
    'm_second_names': [],
}


def load_names():
    global names
    for name, collection in names.items():
        file = f'.\\names\\{name}.txt'
        if os.path.isfile(file):
            with open(file, 'r', encoding='utf-8') as file:
                names[name] = [line.strip() for line in file.readlines()]


def get_random_item(collection):
    return collection[random.randrange(len(collection))]


def get_person(is_male):
    if is_male:
        ln = get_random_item(names['m_last_names'])
        fn = get_random_item(names['m_first_names'])
        sn = get_random_item(names['m_second_names'])
    else:
        ln = get_random_item(names['f_last_names'])
        fn = get_random_item(names['f_first_names'])
        sn = get_random_item(names['f_second_names'])
    return ln, fn, sn


def gen_studs(count):
    result = []
    for i in range(count):
        m_last_name = get_random_item(names['m_last_names'])
        f_last_name = [x for x in names['f_last_names'] if str(x).startswith(m_last_name[:-3])]
        if len(f_last_name) == 0:
            f_last_name = get_random_item(names['f_last_names'])
        else:
            f_last_name = f_last_name[0]

        ln, fn, sn = get_person(False)
        mother = Parent(f_last_name, fn, sn)
        ln, fn, sn = get_person(True)
        father = Parent(m_last_name, fn, sn)

        s = random.choice([True, False])
        ln, fn, sn = get_person(s)
        if s:
            ln = m_last_name
        else:
            ln = f_last_name

        # TODO fix student second name

        result.append(Student(ln, fn, sn, mother, father))
    return result


def gen_teachers(count):
    result = []
    for i in range(count):
        ln, fn, sn = get_person(random.choice([True, False]))
        result.append(Teacher(ln, fn, sn, get_random_item(lessons)))
    return result


def gen_class_groups(count):
    result = []
    teachers = gen_teachers(len(lessons)*2)
    for i in range(count):
        while True:
            group = ClassGroup(f'{random.choice(string.digits[1:])}{random.choice("АБВГД")}')
            if group.name not in [r.name for r in result]:
                break

        group.add_students(gen_studs(10))
        for i in range(len(lessons)):
            k = 0
            while True:
                t = random.choice(teachers)
                if t.lesson_subject not in group.lesson_teacher.keys() or k == 10:
                    break
                k += 1

            if k >= 10:
                continue
            group.set_lesson_teacher(t)
        result.append(group)
    return result


def main():
    load_names()
    school = School()
    school.class_groups = gen_class_groups(10)
    print('1. Получить полный список всех классов школы')
    print('Полный список всех классов школы')
    print(','.join(sorted(school.get_all_classes_names())))
    print('-'*50)

    print('2. Получить список всех учеников в указанном классе')
    gr = get_random_item(school.class_groups)
    print(f'Случайный класс - {gr.name}:')
    print('\n'.join(sorted(gr.get_all_student_names())))
    print('-' * 50)

    print('3. Получить список всех предметов указанного ученика')
    st = get_random_item(school.get_all_students())
    print(f'Случайный ученик - {st.__str__()}:')
    print('\n'.join(list(st.class_group.lesson_teacher.keys())))
    print('-' * 50)

    print('4. Узнать ФИО родителей указанного ученика')
    st = get_random_item(school.all_studs)
    print(f'Случайный ученик - {st.__str__()}:')
    print(f'Mother - {st.mother}\nFather - {st.father}')
    print('-' * 50)

    print('5. Получить список всех Учителей, преподающих в указанном классе')
    gr = get_random_item(school.class_groups)
    print(f'Случайный класс - {gr.name}:')
    print('\n'.join([t.__str__() for t in gr.lesson_teacher.values()]))


if __name__ == '__main__':
    main()
