meaning = int(input('Введите значение диагонали воображаемого квадрата: '))
symbol = input('Введите символ из которого будет написан крест: ')
count = meaning
for row in range(meaning + 1):
    for col in range(meaning + 1):
        if col == row:
            print(f'{symbol}', end='')
        elif col == count:
            print(f'{symbol}', end='')
        else:
            print(' ', end='')
    count -= 1
    print()