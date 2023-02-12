# Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2  bc a_3 a_4 d c_1 d_1 d_2
# from random import randint
import os
os.system('cls')

str_lst = 'a a a b c a a d c d d'
lst_no_sort = str_lst.split(' ')
print(*lst_no_sort)
set_unic = set(lst_no_sort)
lst_unic = list(set_unic)
count = 0
j = 0
while j<len(lst_unic):
     for i in range(len(lst_no_sort)):
     
          if lst_no_sort[i] == lst_unic[j]:
                             
               lst_no_sort[i]=(f'{lst_no_sort[i]}_{count}')
               count += 1
          else :
               lst_no_sort[i]=(f'{lst_no_sort[i]}')
               i +=1       
     count = 0             
     j +=1    

print (*lst_no_sort)          