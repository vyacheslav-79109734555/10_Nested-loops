size = int(input('Введите размер таблицы: '))
for row in range(size):
    for col in range(size):
        print(row + col * 2, end=' \t')
    print()

size = int(input('Введите размер таблицы: '))
for row in range(size):
    for col in range(row, row + size * 2, 2):
        print(col, end='\t')
    print()
