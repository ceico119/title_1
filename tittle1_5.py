from math import sqrt


x1 = int(input('Введите координату x1 '))
y1 = int(input('Введите координату y1 '))
x2 = int(input('Введите координату x2 '))
y2 = int(input('Введите координату y2 '))

distanse = sqrt((x2-x1)**2 + (y2-y1)**2)
print('Расстояние между точками - ', distanse)