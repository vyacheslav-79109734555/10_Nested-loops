print('Цифры больше пяти')
'''
Пользователь вводит последовательность из N чисел. Напишите программу,
которая подсчитывает общее количество цифр больше пяти во всей последовательности.
'''

while True:
    seqNum = input('Сколько будет чисел?: ')
    if seqNum.isdigit():
        print('ok ', end='')
        break
    print('Вы ввели букву: ')
print('Подсчитаем количество цифр больше 5')
count_numb = 0
for num in range(int(seqNum)):
    print('Введите', num + 1, '-е число: ', end='')
    number = int(input())
    while number > 0:
        if number > 5:
            count_numb += 1
        number //= 10
print('Цыфра больше 5 в числах встречается:', count_numb, 'раз')