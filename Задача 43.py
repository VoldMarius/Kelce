# Задача №43.
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках.
# Ввод:            Вывод:
# 1 2 3 2 3         2
from module import creat_list
import os
os.system('cls')

n = int(input('Введите колличество элементов последовательности число N: '))
numm_list = creat_list(n)
print(*numm_list)
numm_list.sort()
print(*numm_list)
count = 0
par = 0
for i in range(1, len(numm_list)):
    if numm_list[i] == numm_list[i-1]:
        count = count + 1
if count > 3:
    count = count + (count-3)


print(count)
