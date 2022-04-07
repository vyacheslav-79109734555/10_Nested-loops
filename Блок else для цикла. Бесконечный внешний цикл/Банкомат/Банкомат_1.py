for attempt in range(1, 4):
    pincode = int(input('Введите ПИН код: '))
    if pincode == 1234:
        print('Пин-код верный ! Держите вашу зарплату !')
        break
    print('Неверный ПИН-код, попыток осталось:', 3 - attempt)
else:
    print('Ваша карта заблокирована. До свидания')
