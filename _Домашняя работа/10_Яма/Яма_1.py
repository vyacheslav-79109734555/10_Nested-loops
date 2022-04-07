numb = int(input('Введите число N: '))
for x in range(numb, 0, -1):
    for n_left in range(numb, 0, -1):
        if x - 1 < n_left:
            print(n_left, end='')
        else:
            print('.', end='')
    for i in range(0, numb + 1):
        if x - 1 < i:
            print(i, end='')
        else:
            print('.', end='')
    print()
