print('Задача 9. Пирамидка 2')
'''
Напишите программу,
которая получает на вход количество уровней пирамиды и выводит их на экран,
Пример:

                vfvf
            vfvf    vfvf
        vfvf    vfvf    vfvf
    vfvf    vfvf    vfvf    vfvf
vfvf    vfvf    vfvf    vfvf    vfvf
'''

n = int(input('Введите количество уровней пирамиды: '))
a = input('Введите символ: ')
l = len(str(a))
for i in range(n):  # 0, 1, 2, 3
    print(' ' * l * (n - 1 - i) + (str(a) + ' ' * l) * (i + 1) + ' ' * l * (n - 2 - i))
