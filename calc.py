# Главная программа - Калькулятор

import modul_1, modul_2, modul_3, modul_4, modul_5, modul_6, modul_7, modul_8, modul_9, modul_10, modul_11, modul_12, modul_13

while True:
    print('\nПеречень возможных операций:\n\nsum - сумма двух чисел\nrazn - разность двух чисел\numn - умножение двух чисел\ndelenie - деление двух чисел\nstepen - возведение в степень\nsrednee - среднее арифметическое двух чисел\ndvoich - перевод числа в двоичную форму\nvosm - перевод числа в восьмиричную форму\nshestn - перевод числа в шестнадцетиричную форму\nfacto - нахождение факториала числа\nkoren - квадратный корень из числа\nkorenis - корень n-ой степени из числа\nexit - выход из программы\nuravn - решение квадратного уравнения\n\n')
    operation = input('Введите операцию: ')

    if operation == 'sum':
        number1 = int(input('Введите первое слагаемое: '))
        number2 = int(input('Введите второе слагаемое: '))
        
        print(number1, '+', number2, '=', modul_1.summa(number1, number2))

    elif operation == 'razn':
        number1 = int(input('Введите уменьшаемое: '))
        number2 = int(input('Введите вычитаемое: '))

        print(number1, '-', number2, '=', modul_2.razn(number1, number2))

    elif operation == 'umn':
        number1 = int(input('Введите множимое: '))
        number2 = int(input('Введите множитель: '))

        print(number1, '*', number2, '=', modul_3.umn(number1, number2))

    elif operation == 'delenie':
        number1 = int(input('Введите делимое: '))
        number2 = int(input('Введите делитель: '))

        print(number1, '-', number2, '=', modul_4.delenie(number1, number2))

    elif operation == 'stepen':
        number1 = int(input('Введите основание степени: '))
        number2 = int(input('Введите показатель степени: '))

        print(number1, '^', number2, '=', modul_5.stepen(number1, number2))

    elif operation == 'srednee':
        number1 = int(input('Введите первое число: '))
        number2 = int(input('Введите второе число: '))

        print('Среднее чисел:', number1,'и', number2, '=', modul_6.srednee(number1, number2))

    elif operation == 'dvoich':
        number1 = int(input('Введите число: '))

        print('Двоичное представление числа:', number1, '=', modul_7.dvoich(number1))

    elif operation == 'vosm':
        number1 = int(input('Введите число: '))

        print('Восьмеричное представление числа:', number1, '=', modul_8.vosm(number1))

    elif operation == 'shestn':
        number1 = int(input('Введите число: '))

        print('Шестнадцатеричное представление числа:', number1, '=', modul_9.shestn(number1))

    elif operation == 'facto':
        number1 = int(input('Введите число: '))

        print('Факториал числа:', number1, '=', modul_10.facto(number1))

    elif operation == 'koren':
        number1 = int(input('Введите число: '))

        print('Квадратный корень числа:', number1, '=', modul_11.koren(number1))

    elif operation == 'korenis':
        number1 = int(input('Введите подкоренное выражение: '))
        number2 = int(input('Введите степень корня: '))

        print('Корень {}-степени из числа {} равен {}'.format(number2, number1, modul_12.korenis(number1, number2)))

    elif operation == 'uravn':
        number1 = int(input('Введите коэффициент a: '))
        number2 = int(input('Введите коэффициент b: '))
        number3 = int(input('Введите коэффициент c: '))

        print('Решения квадратного уравнения:', modul_13.uravn(number1, number2, number3))


    elif operation == 'exit':
        print('\nВыполнение программы завершено\n')
        break
