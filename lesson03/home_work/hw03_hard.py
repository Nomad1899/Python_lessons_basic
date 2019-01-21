# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def fractions_summ(a):
    answer = 0
    x = 0
    y = 0
    n = 0
    n1 = 0
    n2 = 0
    variables = a.split(' ')
    if len(variables) == 3:
        x1 = int(variables[0][:variables[0].index('/')])
        y1 = int(variables[0][variables[0].index('/') + 1:])
        x2 = int(variables[2][:variables[2].index('/')])
        y2 = int(variables[2][variables[2].index('/') + 1:])
    elif len(variables) == 5:
        n1 = int(variables[0])
        n2 = int(variables[3])
        x1 = int(variables[1][:variables[1].index('/')])
        y1 = int(variables[1][variables[1].index('/') + 1:])
        x2 = int(variables[4][:variables[4].index('/')])
        y2 = int(variables[4][variables[4].index('/') + 1:])
    elif len(variables) == 4:
        try:
            n1 = int(variables[0])
            x1 = int(variables[1][:variables[1].index('/')])
            y1 = int(variables[1][variables[1].index('/') + 1:])
            x2 = int(variables[3][:variables[3].index('/')])
            y2 = int(variables[3][variables[3].index('/') + 1:])
        except:
            n2 = int(variables[2])
            x1 = int(variables[0][:variables[0].index('/')])
            y1 = int(variables[0][variables[0].index('/') + 1:])
            x2 = int(variables[3][:variables[3].index('/')])
            y2 = int(variables[3][variables[3].index('/') + 1:])
    else:
        return 'Ввод не соответствует заданному стандарту n1 x1/y1 + n2 x2/y2 '
    if variables.count('-') == 1:
        n2 *= -1
        x2 *= -1
    if abs(y1) == abs(y2):
        n = n1 + n2
        x = x1 + x2
        y = y1
    elif abs(y1) != abs(y2):
        y = y1 * y2
        x = x1 * y2 + x2 * y1
        n = n1 + n2
    if x >= y:
        n += 1
        x = x - y
    for i in range(2, x + 1):
        if x % i == 0 and y % i == 0:
            x = int(x / i)
            y = int(y / i)
            break
    if x!=0:
        return "{} {}/{}".format(n, x, y)
    else:
        return "{}".format(n)


f = '2 3/8 + 3/4'
print(fractions_summ(f))

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
