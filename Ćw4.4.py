class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
    def idzWgóre(self, kroki):
        self.y += kroki * self.krok
    def idzWdół(self, kroki):
        self.y -= kroki * self.krok
    def idzWlewo(self, kroki):
        self.x -= kroki * self.krok
    def idzWprawo(self, kroki):
        self.x += kroki * self.krok
    def gdzieJestes(self):
        print('Pozycja :  (' + str(self.x) + ', ' + str(self.y)+')') 
    def gdzieJestes1(self):
        print('Pozycja końcowa :  (' + str(self.x) + ', ' + str(self.y)+')') 
    def znisz(self):
        print('Robaczek został unicestwiony')
obiekt = Robaczek(3, 5, 2)
obiekt.gdzieJestes()
obiekt.idzWdół(10)
obiekt.idzWgóre(3)
obiekt.idzWprawo(21)
obiekt.idzWlewo(20)
obiekt.gdzieJestes1()

        
    
 
    


