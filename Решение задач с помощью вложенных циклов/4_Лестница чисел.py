print('Лестница чисел')
'''
Пользователь вводит число N. Напишите программу, которая
по этому числу выводит лестницу из чисел:
'''

while True:
    numb = input('Введите размер таблицы: ')
    if numb.isdigit():
        print('ok')
        break
    print('Вы ввели букву: ')
numb = int(numb)
for row in range(1, numb):
    for col in range(row, numb):
        if row % 10 == 0:
            print(row, end='\t')
        else:
            print(col, end='\t')
    print()
