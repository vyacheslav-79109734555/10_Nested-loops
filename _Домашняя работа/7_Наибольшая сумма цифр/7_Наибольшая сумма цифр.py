print('вычисление будет выполнено при ENTER = 0')
number = int(input('Введите число: '))
max_result = 0
max_number = 0
while number != 0:
    meaning = number
    counter = 0
    while number > 0:
        counter += number % 10
        number //= 10
    if counter > max_result:
        max_result = counter
        max_number = meaning
    number = int(input('Введите число: '))
print('Максимальная сумма цифр:', max_result, 'находиться в числе:', max_number)
