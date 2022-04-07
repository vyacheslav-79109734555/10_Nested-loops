height = int(input('Введите высоту рамки: '))
width = int(input('Введите ширину рамки: '))
for row in range(height):
    for col in range(width):
        if row == 0 or row == height - 1:
            print('-', end='\t')
        elif col == 0 or col == width - 1:
            print('|', end='\t')
        else:
            print('', end='\t')
    print()
