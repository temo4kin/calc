# Модуль №7 Перевод десятичного числа в двочное

def dvoich(number1):

    '''Число number1 из десятичного представления переводится в двоичное'''

    chislo = bin(number1)

    number1 = int(chislo[2:])
    
    return(number1)
