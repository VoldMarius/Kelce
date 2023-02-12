# Задача №29.
# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить значение наибольшего элемента
# последовательности, которая завершается первым встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Ваня:                 Петя:
# n = int(input())      n = int(input())
# max_number = 1000     max_number = -1
# while n != 0:         while n < 0:
# n = int(input())      n = int(input())
# if max_number > n:    if max_number < n:
# max_number = n        n = max_number
# print(max_number)     print(n)
from random import randint
import os
os.system('cls')

n = int(input('Введите колличество элементов последовательности число N: '))
start = int(input('Введите начало  последовательности элементов число - S: '))
# sequence = []
# sequence_to_zero = []
# maximum =0
# for i in range(start, n+start):
#     sequence.append(i)
# print(*sequence)

# for i in range(len(sequence)):
#     if  sequence[i]%10 ==0:
#         print(sequence[i])
#         maximum = sequence[i]
#         break     
       
# print(maximum)
sequence = []
sequence_to_zero = []
maximum =0
for i in range(start, n+start):
    sequence.append(randint(start, n+start))
print(*sequence)

for i in range(len(sequence)):
    if  sequence[i]%10 ==0:
        sequence_to_zero = sequence[:i+1]
        print(max(sequence_to_zero))
        break     
    elif i == len(sequence)-1:
        print('нyля - не встретелось')
        
