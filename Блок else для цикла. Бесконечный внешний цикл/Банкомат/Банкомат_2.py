attempt_Count = 3
for attempt in range(1, 4):
    pincode = int(input('Введите ПИН код: '))
    if pincode == 1234:
        print('Пин-код верный ! Держите вашу зарплату !')
        break
    attempt_Count -= 1
    print('Неверный ПИН-код, попыток осталось:', 3 - attempt)
if attempt_Count == 0:
    print('Ваша карта заблокирована. До свидания')