# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib_nums = [1, 1]
    a, b = 1, 1
    for i in range(2, m):
        a, b = b, a + b
        fib_nums.append(b)
    return fib_nums[n - 1:m]


print(fibonacci(3, 7))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    sort = origin_list
    for i in range(0, len(sort)):
        minimum = min(sort[i:])
        if sort[i] > minimum:
            sort[sort[i:].index(minimum) + i] = sort[i]
            sort[i] = minimum
    return sort


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

a = [1, 2, 3, 4, 5]


def func(x):
    return x * 2


def my_filter(func, a):
    b = []
    for i in a:
        b.append(func(i))
    return b


print(my_filter(func, a))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
coordinates = []





def par(coordinates):
    coor = []
    x = 0
    y = 0
    for i in range(1, len(coordinates)):
        for n in range(0, 2):
            if coordinates[0][n] == coordinates[i][n]:
                coor.append(coordinates[0])
                coor.append(coordinates[i])
                coordinates.pop(i)
                coordinates.pop(0)
                if coordinates[0][n] == coordinates[1][n] and abs(coor[0][n - 1] - coordinates[0][n - 1]) == abs(coor[1][n - 1] - coordinates[1][n - 1]):
                    return True
                    break
                else:
                    return False



            else:
                return False


print (par([[10,2],[10,8],[8,0],[8,6]]))