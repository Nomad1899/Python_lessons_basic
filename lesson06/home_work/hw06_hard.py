# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import shutil
import sys


class Worker:
    __first_name: str
    __last_name: str
    job_title: str
    salary = 0
    hours_normal = 0
    hours_completed = 0

    # @property
    # def salary(self):
    #     return self.salary


    @property
    def first_name(self):
        return self.__first_name
    @property
    def last_name(self):
        return self.__last_name
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __init__(self, data_line: str):
        worker_data = data_line.split()
        self.__first_name = worker_data[0]
        self.__last_name = worker_data[1]
        self.salary = int(worker_data[2])
        self.job_title = worker_data[3]
        self.hours_normal = worker_data[4]

workers=[]
completed = []



path='data/workers'
with open(path, encoding="UTF-8",) as f:

    workers_list = f.readlines()[1:]

    for line in workers_list:
        workers.append(Worker(line))

with open('data/hours_of',encoding="UTF-8") as f:
    hours_list = f.readlines()[1:]

    for line in hours_list:
        dict_keys = ['firstname', 'lastname', 'completed']
        dict_values = line.split()

        item = dict(zip(dict_keys, dict_values))
        item['completed'] = int(item['completed'])

        completed.append(item)


for p in workers:
    print(p.salary)







