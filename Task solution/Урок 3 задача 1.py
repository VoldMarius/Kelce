# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint
import os
os.system('cls')

n = int(input('Введите число N: '))
numm_list = []
odd_number=[]
for i in range(n):
    numm_list.append(randint(-2, n))
summ = 0
for i in range(1,len(numm_list),2):
    if i % 2 != 0:
       odd_number.append(numm_list[i])   
print(f'{numm_list} -> на нечётных позициях элементы {(odd_number)} , ответ: {(sum(odd_number))}' )      