count_numb = 0
n = int(input('Введите кол-во чисел: '))
for number in range(n):
    num = int(input(f'Введите {number + 1} число: '))
    if num != 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3) and (num % 5 != 0 or num == 5):
        count_numb += 1
print(f'\nпростых чисел {count_numb}')
