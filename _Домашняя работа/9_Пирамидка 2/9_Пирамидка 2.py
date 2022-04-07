number = int(input('Введите количество уровней пирамиды: '))
count = 1
retreat = number * 4
for row in range(number):
    retreat -= 3
    print(' ' * retreat, end='')
    for num in range(row + 1):
        print(count, ' ' * (number - 1), end='')
        count += 2
    print()
