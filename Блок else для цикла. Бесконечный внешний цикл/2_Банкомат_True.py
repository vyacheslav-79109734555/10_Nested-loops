

while True:
    for attempt in range(1, 4):
        while True:
            pincode = input('Введите ПИН код: ')
            if pincode.isdigit():
                print('', end='')
                break
            print('что то пошло не так ! попробуй еще раз: ')
        pincode = int(pincode)
        if pincode == 1234:
            print('\nПин-код верный ! Держите вашу зарплату !')
            break
            print('Неверный ПИН-код, попыток осталось:', 3 - attempt)
    else:
        print('\nВаша карта заблакирована. Досвидания')
    print('\nСледующий клиент, Добро пожаловать ! ')
