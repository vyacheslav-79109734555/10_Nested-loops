number = int(input('Введите высоту пирамиды: '))
symbol = 1
for num in range(number):
    print(' ' * (number - 1 - num), '#' * symbol)
    symbol += 2
