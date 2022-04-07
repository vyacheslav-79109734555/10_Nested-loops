n = int(input('Введите кол-во чисел: '))
numberCount = 0
flag = 0

for number in range(n):
    num = int(input('Введите число: '))
    for x in range(num - 1, 1, -1):
        if num % x == 0:
            flag = 1
    if num != 1 and flag == 0:
        numberCount += 1
    flag = 0

print(f'Кол-во простых чисел в последовательности = {numberCount}')
