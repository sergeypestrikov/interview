# Разработать генератор случайных чисел. В функцию передавать начальное и конечное число
# генерации (нуль необходимо исключить). Заполнить этими данными список и словарь.
# Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
# Вывести содержимое созданных списка и словаря.
import random


def nums_generator(a, b):
    num_list = []
    num_dict = {}
    for nums in range(20):
        result = int((b - a) * random.random() + a)
        num_list.append(result)
        num_dict.update({'elem_{}'.format(result): result})

    return (num_list, num_dict)


print(nums_generator(2, 5))