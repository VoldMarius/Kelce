# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint
import os
os.system('cls')


def MultiplList(numm, k):
    multipl = []
    if k % 2 == 0:
        length = k//2
        for i in range(length):
            multipl.append(numm[i] * numm[k-1-i])
    else:
        length = k//2+1
        for i in range(length):
            multipl.append(numm[i] * numm[k-1-i])
    return multipl


n = int(input('Введите число N: '))
numm_list = []
for i in range(n):
    numm_list.append(randint(-2, n))

print(numm_list)
print(MultiplList(numm_list, n))
