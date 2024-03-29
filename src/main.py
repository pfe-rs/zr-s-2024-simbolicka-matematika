from lib.lib import *

x = Simbol("x")
y = Simbol("y")
z  =Simbol("z")

br = Broj(0)

br2=Broj(0.75)
izr=x-z+z+x+y

jedan = Broj(1)
izr1= izr.subs(x, jedan).subs(y, jedan).subs(z, jedan)
print(izr1)

print(x+y==y+x)