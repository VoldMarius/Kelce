from random import randint
numm_list = []
count = 0
for i in range(10):
    numm_list.append(randint(-5,5))
print(numm_list)
for i in range(1,10):
    if numm_list [i-1]<numm_list [i]:
        print (f'{numm_list [i-1]} < {numm_list [i]}')
        count +=1
print(f'кол-во элементов больших предыдущего-> {count}') 