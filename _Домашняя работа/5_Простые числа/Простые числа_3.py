count_numb = 0
begin_number = int(input('Введите первое значение последовательности чисел : '))
end_number = int(input('Введите последнее значение последовательности чисел : '))
print('Простые числа в списке:')
for num in range(begin_number, end_number + 1):
    if num != 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3) and (num % 5 != 0 or num == 5):
        print(num, end='\t')
        count_numb += 1
print('\nпростых чисел', count_numb)
