

class Izraz:
    def __init__(self, ceo, realan, pozitivan, negativan, nula):
        self._ceo=ceo
        self._realan=realan
        self._pozitivan=pozitivan
        self._negativan = negativan
        self._nula = nula
    def __neg__(self):
        pass
        #return Neg.simplify(self)
    def __eq__(self, b):
        pass
        #return self==b?
    
    def __add__(self, b):
        pass
        #return Add,.simplify(self, b)
    
    def __sub__(self, b):
        pass
        #return Sub.simplify(self, b)
    
    def simplify():
        return
    
    def collect():
        return
    
    def __str__(self):
        return
    
    
class Simbol(Izraz): #podrazumevano je realan
    def __init__(self, ime, ceo=False, realan=True, pozitivan=None, negativan=None, nula=None):
        if(pozitivan and negativan):
            raise ("Broj ne moze biti i pozitivan i negativan!!!")
        self._ime = ime
        super().__init__(ceo, realan, pozitivan, negativan, nula)

class Broj(Izraz): #podrazumevano je realan
    def __init__(self, vrednost, ceo=False, realan=True, pozitivan=None, negativan=None, nula=None):
        self._vrednost = vrednost
        super().__init__(ceo, realan, pozitivan, negativan, nula)
class Neg(Izraz):
    def __init__(self, izraz):
        self._izraz = izraz
        ceo = izraz._ceo
        realan = izraz._realan
        if izraz._pozitivan==True:
            pozitivan = False
            negativan = True
        elif izraz._negativan == True:
            pozitivan = True
            negativan = False
        else:
            pozitivan=None
            negativan=None

        nula = izraz._nula

        super().__init__(ceo, realan, pozitivan, negativan, nula)

    def simplify(izraz):
        if isinstance(izraz, Neg):
            return izraz._izraz
        else:
            return Neg(izraz)
