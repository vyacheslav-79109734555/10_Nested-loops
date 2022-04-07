x = int(input('\nВведите высоту пирамиды: '))
for i in range(x):
    print('% s % s' % (' ' * (x - i - 1), '*' * (i * 2 + 1)))
