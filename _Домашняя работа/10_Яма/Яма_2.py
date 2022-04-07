numb = int(input('\nВведите число N: '))
for x in range(numb):
    for n_left in range(numb, numb - x - 1, -1):
        print(n_left, end=' ')
    countDot = n_left * 2 - 2
    print(' .' * countDot, end=' ')
    for n_right in range(n_left, numb + 1):
        print(n_right, end=' ')
    print()
