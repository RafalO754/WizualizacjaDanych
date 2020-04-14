import math

a = input('Podaj pierwszą liczbę : ')
b = input('Podaj drugą liczbę : ')
c = input('Podaj trzecią liczbę : ')

if (int(a) > 0 and int(a) < 10) and (int(b) > 0 and int(b) < 10) and (int(c) > 0 and int(c) < 10) and (int(a) > int(b) or int(b) > int(c) ) :
    print('Warunki spełnione')
else:
    print('Warunki niespełnione')



