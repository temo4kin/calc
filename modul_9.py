# Модуль №9 Перевод десятичного числа в шестнадцатиричное

def shestn(number1):

    '''Число number1 из десятичного представления переводится в шестнадцатиричное'''

    chislo = hex(number1)

    number1 = int(chislo[2:])
    
    return(number1)
