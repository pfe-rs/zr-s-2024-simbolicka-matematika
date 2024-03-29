


class Izraz:
    def __init__(self, ceo, realan, pozitivan, negativan, nula):
        c = 0
        if pozitivan: c+=1
        if negativan: c+=1
        if nula: c+=1
        if(c>1):
            raise Exception("Los tip!!!")
        
        if(not ceo and not realan):
            raise Exception("Los tip!!!")
        self._ceo=ceo
        self._realan=realan
        self._pozitivan=pozitivan
        self._negativan = negativan
        self._nula = nula
        
    def __neg__(self):
        return Neg.simplify(self)

    def __eq__(self, b):
        if isinstance(self, Simbol):
            if self._ime==b._ime:
                return True
            else:
                return False
        elif isinstance(self, Broj):
            if self._vrednost==b._vrednost:
                return True
            else:
                return False
        else:
            if not (len(self.lista)==len(b.lista)):
                return False
            for i in range(len(self.lista)):
                if self.lista[i]==b.lista[i]:
                    pass
                else:
                    return False
            return True

        pass
        # return self==b?

    def __add__(self, b):
        return Add.simplify(self, b)

    def __sub__(self, b):
        pass
        # return Sub.simplify(self, b)

    def simplify():
        return

    def collect():
        return

    def __str__(self):
        return
    
    def subs(izraz, iz , u):
        for i in range(len(izraz.lista)):
            nesto = izraz.lista[i]
            if isinstance(nesto, Simbol):
                if(nesto._ime==iz._ime):
                    izraz.lista[i] = u
            elif not isinstance(nesto, Broj):
                Izraz.subs(nesto, iz, u)
        return izraz
    
    
class Simbol(Izraz): #podrazumevano je realan
    def __init__(self, ime, ceo=False, realan=True, pozitivan=None, negativan=None, nula=None):
        self._ime = ime
        super().__init__(ceo, realan, pozitivan, negativan, nula)
    def __str__(self):
        return f"{self._ime}"


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
            return izraz
        elif isinstance(izraz, Neg):
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
   

class Broj(Izraz):  # podrazumevano je realan
    def __init__(self, vrednost, ceo=False, realan=True, pozitivan=None, negativan=None, nula=None):
        self._vrednost = vrednost
        super().__init__(ceo, realan, pozitivan, negativan, nula)

    def __str__(self):
        return f"{str(self._vrednost)}"


class Add(Izraz):
    def __init__(self, a, b):  # a + b
        self.lista = [a, b]

        ceo = None
        realan = None
        pozitivan = None
        negativan = None
        nula = None
        
        if a._ceo and b._ceo:
            ceo = True

        if a._ceo and b._realan:
            realan = True

        if a._realan and b._ceo:
            realan = True

        if a._realan and b._realan:
            realan = True

        if a._pozitivan and b._pozitivan:
            pozitivan = True

        if a._negativan and b._negativan:
            negativan = True

        if a._nula and b._nula:
            nula = True

        if a._nula and b._ceo:
            ceo = True

        if a._nula and b._realan:
            realan = True

        if a._nula and b._negativan:
            negativan = True

        if a._nula and b._pozitivan:
            pozitivan = True

        if b._nula and a._ceo:
            ceo = True

        if b._nula and a._realan:
            realan = True

        if b._nula and a._negativan:
            negativan = True

        if b._nula and a._pozitivan:
            pozitivan = True
        
        super().__init__(ceo,realan, pozitivan, negativan,nula)

    def simplify(a, b):
        if isinstance(a, Broj) and isinstance(b, Broj):
            vred = a._vrednost + b._vrednost
            ceo=False
            realan=False
            nula=False
            poz=False
            neg=False
            if isinstance(vred, int):
                ceo = True
            else:
                realan=True
            if vred==0:
                nula  =True
            elif vred>0:
                poz = True
            else:
                neg = True
            x = Broj(vred, ceo, realan, poz, neg, nula)
            return x
        return Add(a, b)

    def __str__(self):
        a = ""
        for x in self.lista:
            if (len(a) > 0): a = a + " + "
            a = a + x.__str__()
        return a 
