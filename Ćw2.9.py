liczba = input('Podaj liczbę wielocyfrową : ')
a = int(liczba)
suma = 0
while (a != 0):
    suma = suma + (a % 10)
    a = a // 10
print("Suma cyfr liczby " + str(liczba) + " wynosi " + str(suma))


 
