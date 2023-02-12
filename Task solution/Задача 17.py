# Задача №17.
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
from random import randint
import os
os.system('cls')

n = int(input('Введите число N: '))
numm_list = []
for i in range(n):
    numm_list.append(randint(-2, n))
print(numm_list)
count = 0
numm_list.sort()
for i in range(n):
    if numm_list[i] != numm_list[i-1]:
          count += 1
print(count)