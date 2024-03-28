class Izraz:
    def __init__(self, ceo, realan, pozitivan, negativan, nula):
        c = 0
        if pozitivan: c+=1
        if negativan: c+=1
        if nula: c+=1
        if(c>1):
            raise ("Los tip!!!")
        
        if(not ceo and not realan):
            raise ("Los tip!!!")
        self._ceo=ceo
        self._realan=realan
        self._pozitivan=pozitivan
        self._negativan = negativan
        self._nula = nula
    def __neg__(self):
        if isinstance(self, Broj):
            return Broj(-self._vrednost)
        return Neg(self)
    def __eq__(self, b):
        pass
        #return self==b?
    
class Simbol(Izraz): #podrazumevano je realan
    def __init__(self, ime, ceo=False, realan=True, pozitivan=None, negativan=None, nula=None):
        self._ime = ime
        super().__init__(ceo, realan, pozitivan, negativan, nula)
    def __str__(self):
        return f"{self._vrednost}"
    
class Broj(Izraz): #podrazumevano je realan
    def __init__(self, vrednost, ceo=False, realan=True, pozitivan=None, negativan=None, nula=None):
        self._vrednost = vrednost
        super().__init__(ceo, realan, pozitivan, negativan, nula)
    def __str__(self):
        return f"{self._vrednost}"

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
        if isinstance(izraz, Broj):
            izraz._vrednost=-izraz._vrednost
            return
        if isinstance(izraz, Neg):
            return izraz._izraz
        else:
            return Neg(izraz)
    def __str__(self):
        s = str(self._izraz)
        if s[0] == "-":
            s = s[1:]
        else:
            s = "-" + s
        for i in range(1, len(s)):
            if s[i] == '-':
                s = s[:i] + '+' + s[i+1:]
            elif s[i] == '+':
                s = s[:i] + '-' + s[i+1:]
        return s
