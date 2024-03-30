
class Izraz:
    def __init__(self, ceo, realan, pozitivan, negativan, nula):
        self.lista=[]
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
        if isinstance(b, int):
            b  = Broj(b, ceo=True)
        elif isinstance(b, float):
            b = Broj(b)
        if type(self) == type(b):
            if self.lista == b.lista:
                return True
        return False

    def __add__(self, b):
        if isinstance(b, int):
            b  = Broj(b, ceo=True)
        elif isinstance(b, float):
            b = Broj(b)

        print(type(b))
        print(b._vrednost)
        return Add.simplify(self, b)
    
    def __pow__(self, b):
        if isinstance(b, int):
            b  = Broj(b, ceo=True)
        elif isinstance(b, float):
            b = Broj(b)
        return Pow.simplify(self, b)

    def __sub__(self, b):
        if isinstance(b, int):
            b  = Broj(b, ceo=True)
        elif isinstance(b, float):
            b = Broj(b)
        return Sub.simplify(self, b)
    
    def __mul__(self, b):
        if isinstance(b, int):
            b  = Broj(b, ceo=True)
        elif isinstance(b, float):
            b = Broj(b)
        return Mul.simplify(self, b)
    def __truediv__(self, b):
        if isinstance(b, int):
            b  = Broj(b, ceo=True)
        elif isinstance(b, float):
            b = Broj(b)
        return Div.simplify(self, b)

    @staticmethod
    def simplify(izraz):
        for el in izraz.lista:
            return el.simlify(izraz)

    def __str__(self):
        return
    
    def subs(self, mapa):
        for i in range(len(self.lista)):
            nesto = self.lista[i]
            for iz, u in mapa:
                if nesto == iz:
                    self.lista[i] = u
                elif nesto == Neg(iz):
                    self.lista[i] = Neg(u)
                elif isinstance(nesto, Izraz):
                    nesto.subs(mapa)
        return self
    
class Simbol(Izraz): #podrazumevano je realan
    def __init__(self, ime, ceo=False, realan=True, pozitivan=None, negativan=None, nula=None):
        self._ime = ime
        super().__init__(ceo, realan, pozitivan, negativan, nula)
        self.lista.append(ime)
    def __str__(self):
        return f"{self._ime}"
    def __repr__(self) -> str:
        return f"Simbol({self._ime})"


class Broj(Izraz): #podrazumevano je realan
    def __init__(self, vrednost, ceo=False, realan=True, pozitivan=None, negativan=None, nula=None):
        self._vrednost = vrednost
        super().__init__(ceo, realan, pozitivan, negativan, nula)
        self.lista.append(vrednost)
    def __str__(self):
        return f"{self._vrednost}"
    def __repr__(self) -> str:
        return f"Broj({self._vrednost})"

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
        self.lista.append(izraz)

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
        return "( "+ s+ " )"
   

class Broj(Izraz):  # podrazumevano je realan
    def __init__(self, vrednost, ceo=False, realan=True, pozitivan=None, negativan=None, nula=None):
        self._vrednost = vrednost
        super().__init__(ceo, realan, pozitivan, negativan, nula)

    def __str__(self):
        return f"{str(self._vrednost)}"


class Add(Izraz):
    def __init__(self, a, b):  # a + b

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
        
        self.lista = [a,b]

    def simplify(a, b):
        if(a == Neg(b)):
            return Broj(0)
        if(a==b):
            dvojka = Broj(2, ceo=True, pozitivan=True)
            return Mul(dvojka, a)
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
        terms = []
        for term in self.lista:
            term_str = term.__str__()
            if term_str and terms:  
                if term_str[0] != '-':
                    terms.append('+' + term_str)
                else:
                    terms.append(term_str)
            else:
                terms.append(term_str)
        t = ''.join(terms)
        
        if len(terms) == 0:
            return "0"
        if terms[0] == '+':
            terms = terms[1:] 
        return "( " + ''.join(terms) + " )"
    
class Sub(Izraz):
    def __init__(self, a, b):  # a + b
       
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

        if a._pozitivan and b._negativan:
            pozitivan = True

        if a._negativan and b._pozitivan:
            negativan = True

        if a._nula and b._nula:
            nula = True

        super().__init__(ceo, realan, pozitivan, negativan, nula)
        if not a == Neg(b):
            self.lista = [a, Neg(b)]

    @staticmethod
    def simplify(a, b):
        if(a == b):
            return Broj(0)
        if isinstance(a, Broj) and isinstance(b, Broj):
            vred = a._vrednost - b._vrednost
            ceo = isinstance(vred, int)
            realan = not ceo
            nula = vred == 0
            poz = vred > 0
            neg = vred < 0
            return Broj(vred, ceo, realan, poz, neg, nula)
        return Sub(a, b)
    def simplify(a, b):
        if isinstance(a, Broj) and isinstance(b, Broj):
            vred = a._vrednost - b._vrednost
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
        return Sub(a, b)

    def __str__(self):
        terms = []
        for term in self.lista:
            term_str = term.__str__()
            if term_str[0] != '-' and terms:
                terms.append('+' + term_str)
            else:
                terms.append(term_str)
        t = ''.join(terms)
        
        return "0" if len(t)==0 else t

class Mul(Izraz):
    def __init__(self, a, b):  # a * b
        ceo = None
        realan = None
        pozitivan = None
        negativan = None
        nula = None
        if a._ceo and b._ceo:
            ceo=True
        else:
            realan = True

        if (a._pozitivan and b._pozitivan) or (a._negativan and b._negativan):
            pozitivan = True
        elif a._nula or b._nula:
            nula = True
        else:
            negativan=True
        
        super().__init__(ceo, realan, pozitivan, negativan, nula)
        self.lista = [a, b]

    @staticmethod
    def simplify(a, b):
        if(a==b):
            return Pow(a, Broj(2,ceo=True,  pozitivan=True))
        return Mul(a, b)

    def __str__(self):
        terms = []
        for term in self.lista:
            term_str = term.__str__()
            if term_str[0] != '-' and terms:
                terms.append(term_str)
            else:
                terms.append(term_str)
        t = " ( " + '*'.join(terms) + " ) "
        
        return t
    
class Div(Izraz):
    def __init__(self, a, b):  # a / b
        ceo = None
        realan = None
        pozitivan = None
        negativan = None
        nula = None

        if b._nula:
            raise Exception("Deljenje nulom!!!!")
        if isinstance(a, Broj) and isinstance(b, Broj) and a._vrednost%b._vrednost==0:
            ceo=True
        else:
            realan = True

        if (a._pozitivan and b._pozitivan) or (a._negativan and b._negativan):
            pozitivan = True
        elif a._nula:
            nula = True
        else:
            negativan=True
        
        super().__init__(ceo, realan, pozitivan, negativan, nula)
        self.lista = [a, b]

    @staticmethod
    def simplify(a, b):
        if a==b:
            return Broj(1, pozitivan=True)
        return Div(a, b)

    def __str__(self):
        terms = []
        for term in self.lista:
            term_str = term.__str__()
            if term_str[0] != '-' and terms:
                terms.append('/ ' + term_str)
            else:
                terms.append(term_str)
        return "( " + ' '.join(terms) + " )"
    
class Pow(Izraz):
    def __init__(self, a, b):  # a / b
        ceo = None
        realan = None
        pozitivan = None
        negativan = None
        nula = None

        
        if a._realan:
            realan=True
        elif b._ceo:
            ceo = True
        else:
            realan = True

        pozitivan=True
        
        super().__init__(ceo, realan, pozitivan, negativan, nula)
        self.lista = [a, b]

    @staticmethod
    def simplify(a, b):
        if not isinstance(b, Broj):
            raise Exception("Eksponent mora biti broj!!!!")
        if b._vrednost==1:
            return a
        return Pow(a, b)

    def __str__(self):
        terms = []
        for term in self.lista:
            term_str = term.__str__()
            if term_str[0] != '-' and terms:
                terms.append('**' + term_str)
            else:
                terms.append(term_str)
        return "( " + ''.join(terms) + " )"