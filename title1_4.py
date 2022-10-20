def qouter(namber_qouter):
    if namber_qouter >= 1 and namber_qouter <= 4:
        if namber_qouter == 1:
            return('Возможный диапазон точек координат:\nX от 0 до + бесконечности \nY от 0 до + бесконечности')
        elif namber_qouter == 2:
            return('Возможный диапазон точек координат:\nX от 0 до - бесконечности \nY от 0 до + бесконечности')
        elif namber_qouter == 3:
            return('Возможный диапазон точек координат:\nX от 0 до - бесконечности \nY от 0 до - бесконечности')
        else:
            return('Возможный диапазон точек координат:\nX от 0 до + бесконечности \nY от 0 до - бесконечности')


namber_qouter = int(input('Введите номер четверти - '))
print(qouter(namber_qouter))