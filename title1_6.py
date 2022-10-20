day = int(input('Введите число от 1 до 7 '))
if day >=1 and day <= 7:    
    if day < 6:
        print('этот день рабочий')
    else:
        print('Ура!!! Выходной!!!')
else:
    print('Вы вышли из диапазона дней недели')