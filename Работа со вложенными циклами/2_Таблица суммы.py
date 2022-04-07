print('Задача 2. Таблица суммы')
'''
Напишите программу, которая запрашивает у пользователя число N и
выводит таблицу суммы для чисел от 1 до N.

'''

numb = int(input('Введите число: '))
for pow in range(numb + 1):
    for col in range(numb + 1):
        print(pow + col, end=' ')
    print(' ')



