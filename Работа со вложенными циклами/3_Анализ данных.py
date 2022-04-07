print('Задача 3. Анализ данных')
'''
Отдел анализа данных сегодня получил вот такую интересную штуку:

'''
numb_1 = int(input('Введите значение строк: '))
numb_2 = int(input('Введите значение столбцов: '))
#
for row in range(numb_1 + 1):
    for col in range(numb_2 + 1):
        print(row - col,  end='\t')
    print()
