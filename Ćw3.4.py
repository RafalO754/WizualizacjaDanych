def monotonicznoscfunkcji(a,b):

    if a<0:

        print("Funkcja y =",a,"* x +",b,"jest malejaca")

        return a

    elif a==0:

        print("Funkcja y =",a,"* x +",b,"jest stała")

        return a

    else:

        print("Funkcja y =",a,"* x +",b,"jest rosnaca")

        return a

print(monotonicznoscfunkcji(-4,3))

print(monotonicznoscfunkcji(-1,5))

print(monotonicznoscfunkcji(7,4))