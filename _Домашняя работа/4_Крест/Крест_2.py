meaning = int(input('Введите значение диагонали воображаемого квадрата: '))
for row in range(meaning + 1):
    for col in range(meaning + 1):
        if col == row or col == -row + meaning:
            print('*', end='')
        else:
            print(' ', end='')
    print()