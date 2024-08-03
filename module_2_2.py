first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')

if first == second == third:
    print('3 числа равны между собой')
elif first == second  or first == third or second == third:
    print('2 числа равны между собой')
else: print('0 чисел равых между собой')