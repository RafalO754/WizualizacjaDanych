class NaZakupy:
    def __init__(self, nazwaProduktu, ilosc, jednostkaMiary, cenaJed):
        self.nazwaProduktu = nazwaProduktu
        self.ilosc = ilosc
        self.jednostkaMiary = jednostkaMiary
        self.cenaJed = cenaJed
    def wyświetlProdukt(self):
        print('Nazwa produktu : ' + str(self.nazwaProduktu))
        print('Ilosc : ' + str(self.ilosc))
        print('Jednostka Miary : ' + str(self.jednostkaMiary))
        print('Cena jednostkowa : ' + str(self.cenaJed))
    def ileProduktu(self):
        return str(self.ilosc) + ' ' + str(self.jednostkaMiary)
    def ileKosztuje(self):
        return self.ilosc * self.cenaJed

obiekt = NaZakupy('Kasza', 30, 'kg', 120)
obiekt.wyświetlProdukt()
print('Ilość produktu : ' + obiekt.ileProduktu())
print('Cena produktu : ' + str(obiekt.ileKosztuje()) + ' PLN')
    
 
    


