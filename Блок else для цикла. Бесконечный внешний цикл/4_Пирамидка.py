print('Задача 9. Пирамидка')
'''
Напишите программу,
которая получает на вход количество уровней пирамиды и выводит их на экран,
Пример:

vfvf    vfvf    vfvf    vfvf    vfvf
    vfvf    vfvf    vfvf    vfvf
        vfvf    vfvf    vfvf
            vfvf    vfvf
                vfvf

'''

n = int(input('Введите количество уровней пирамиды: '))
a = input('Введите символ: ')
l = len(str(a))
for i in list(range(n))[::-1]:
    print(' ' * l * (n - 1 - i) + (str(a) + ' ' * l) * (i + 1) + ' ' * l * (n - 2 - i))
