# Модуль №8 Перевод десятичного числа в восьмеричное

def vosm(number1):

    '''Число number1 из десятичного представления переводится в восьмеричное'''

    chislo = oct(number1)

    number1 = int(chislo[2:])
    
    return(number1)
