print('Ьанкомат')
'''
условие задачи:
на ввод пинкода даёться 3 попытки
при неверном вводе сообщение:
"Неверный пинкод. Осталось попыток: N"
Выходные данные:
Сообщение: "Пин-код верный ! Держите вашу зарплату !"
либо
Сообщение: "Ваша карта заблокирована. До свидания"
'''

...
# attempt_Count = 3
# for attempt in range(1, 4):
#     pincode = int(input('Введите ПИН код: '))
#     if pincode == 1234:
#         print('Пин-код верный ! Держите вашу зарплату !')
#         break
#     attempt_Count -= 1
#     print('Неверный ПИН-код, попыток осталось:', 3 - attempt)
# if attempt_Count == 0:
#     print('Ваша карта заблокирована. До свидания')
...
# ИЛИ с блоком else:

for attempt in range(1, 4):
    pincode = int(input('Введите ПИН код: '))
    if pincode == 1234:
        print('Пин-код верный ! Держите вашу зарплату !')
        break
    print('Неверный ПИН-код, попыток осталось:', 3 - attempt)
else:
    print('Ваша карта заблокирована. До свидания')