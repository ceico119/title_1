def coordinates(x,y):
    qouters_1 = 'I'
    qouters_2 = 'II'
    qouters_3 = 'III'
    qouters_4 = 'IV'
    if x != 0 and y != 0:
        if x > 0 and y > 0:
            return qouters_1
        elif x < 0 and y > 0:
            return qouters_2
        elif x < 0 and y < 0:
            return qouters_3
        else:
            return qouters_4

x = float(input('--Введите координату X '))
y = float(input('--Введите координату Y '))

print(coordinates(x, y))