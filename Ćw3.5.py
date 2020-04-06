def proste_czy_rownolegle(a1, a2):

    if(a1 == a2):

        return 'równoległe'

    if(a1*a2 == -1):

        return 'prostopadłe'

    else:

        return 'ani równoległe ani prostopadłe'



def zadanie_5():

    print('y = ax + b')

    a1 = float(input('Podaj a1: '))

    b1 = float(input('Podaj b1: '))

    a2 = float(input('Podaj a2: '))

    b2 = float(input('Podaj b2: '))

    print('y1 = '+str(a1)+'x + '+str(b1))

    print('y2 = '+str(a2)+'x + '+str(b2))

    print('Proste y1 i y2 są '+str(proste_czy_rownolegle(a1, a2)))