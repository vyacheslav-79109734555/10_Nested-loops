meaning_N = int(input('Введите число N '))
print('находим сумму факториалов 1! + 2! + 3! +... + N!')
sum_factorials = 0
previous_value = 1
for numb in range(1, meaning_N + 1):
    current_factorials = previous_value * numb
    sum_factorials += current_factorials
    previous_value = current_factorials
print('Сумма факториалов от 1! до', meaning_N, 'равна:', sum_factorials)
