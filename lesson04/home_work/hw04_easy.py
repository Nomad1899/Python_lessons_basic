# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
a = [1, 2, 4, 0]
b = [i ** 2 for i in a]
print(b)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
bob_fruits = ['orange', 'Blueberries', 'banana', 'Grapefruit', 'Lemon', 'Mandarin', 'Papaya']
jonh_fruits = ['Peaches', 'Lemon', 'Raspberries', 'Blueberries', 'Mandarin', 'Watermelon']
fruits = [x for x in bob_fruits if x in jonh_fruits]
print (fruits)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random
numbers=[random.randint(0,100) for m in range(10)]
print (numbers)
my_numbers=[x for x in numbers if x%3==0 and x>0 and x%4!=0]
print (my_numbers)
