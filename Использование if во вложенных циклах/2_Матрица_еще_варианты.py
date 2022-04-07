size = int(input('Введите размер таблицы: '))
for row in range(1, size + 1):
    for col in range(1, size + 1):
        if col % 10 == 0:
            print(col, end='\t')
        else:
            print(row, end='\t')
    print()
