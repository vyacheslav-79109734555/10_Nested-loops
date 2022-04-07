while True:
    numb = input('Введите размер таблицы числом: ')
    if numb.isdigit():
        print('ok')
        break
    print('Упс что пошло не так, попробуй еще раз: ')
numb = int(numb)
for row in range(1, numb + 1):
    for col in range(row):
        if row // 100 == 0:
            print(row, end='\t')
        else:
            print(col, end='\t')
    print()
