# Модуль №13 решение квадратного уравнения

def uravn(number1, number2, number3):

    '''нахождение дискриминанта'''

    D = (number2**2) - 4 * number1 * number3

    '''нахождение корней уравнения'''

    if D > 0:
        x1 = (-number2 + (D ** 0.5))/(2 * number1)
        x2 = (-number2 - (D ** 0.5))/(2 * number1)
        return(x1, x2)
    elif D == 0:
        x1 = -number2/(2 * number1)
        x2 = ''
    elif D < 0:
        return('Решений нет')
