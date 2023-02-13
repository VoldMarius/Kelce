# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import random
import os
os.system('cls')


def CreatFloatList(k):
    nummbers_list = []
    for i in range(k):
        nummbers_list.append(round(random(), 2))
    return nummbers_list


# n = int(input('Введите число N: '))

# print(CreatFloatList(n))
# num_list = CreatFloatList(n)
# num_list = (num_list)
num_list = [1.1, 1.2, 3.1, 5, 10.01]

for i in range(5):
    num_list[i] = num_list[i]*100

print  (num_list)     

print((max(num_list)-min(num_list))/100)
