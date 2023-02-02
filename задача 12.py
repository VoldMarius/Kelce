s = int(input('Введите сумму загданных чисел: '))
p = int(input('Введите произведение загданных чисел: '))

for x in range(1,1000):
    for y in range(1,1000):
        if x + y == s and x * y == p:
            print(f'Значение X ->{x} значение Y ->{y} ')