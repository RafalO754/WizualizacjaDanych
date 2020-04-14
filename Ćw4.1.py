liczby = []
for x in range(1, 40, 1):
    if x % 4 == 0:
        liczby += [x]
doc = open('LiczbyDoZadania.txt','w+')
doc.writelines(str(liczby))
doc.close()