print('Последовательность')
'''
Программа посчитает сколько раз встречаеться определённая чыфра в веденных пользователем числах?
'''

seqNum = int(input('Сколько будет чисел?: '))
numeral = int(input('Какую цифру считать?: '))   # цифра
while numeral < 0 or numeral > 9:
    numeral = int(input('Цыфра должна быть в диапазоне от 1 до 9! \nВведите новую цифру: '))
numeral_Count = 0
for num in range(seqNum):
    print('Введите', num + 1, '-е число: ', end='')
    number = int(input())
    while number > 0:
        if number % 10 == numeral:
            numeral_Count += 1
        number //= 10
print('Цыфра:', numeral, 'в числах встречаеться:', numeral_Count, 'раз')
