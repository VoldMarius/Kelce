# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все
# пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую
# пару не дает).
import os
os.system('cls')

k = int(input('Введите натуральное число k,не превосходящее 100_000: '))

dict_divisors = {}
dict_values = {}
count = 0
key_list = []
value_list = []
for i in range(1, k+1):
    for j in range(1, k+1):
        if j == i:
            j += 1
        if i % j == 0:
            count = count + j
            dict_divisors[i] = count
    count = 0

print(dict_divisors)
key_list = list(dict_divisors.keys())
value_list = list(dict_divisors.values())

for i in range(len(dict_divisors)):
    for j in range(len(dict_divisors)):
        if key_list[j] == value_list[i]:
            if key_list[j] != i+2 and i+2 < k:
                dict_values[key_list[j]] = i+2
print(dict_values)
