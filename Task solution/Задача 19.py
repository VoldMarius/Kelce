# Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

from array import array

n = int(input('Введите число N: '))
k = int(input('Введите число К: '))
numm_list = []
for i in range(1,n+1):
    numm_list.append(i)
print(f'{numm_list} K = {k}')
print (numm_list [k:]+numm_list[:k])