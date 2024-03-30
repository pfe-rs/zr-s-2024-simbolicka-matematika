from lib.lib import *

x = Simbol("x")
y = Simbol("y")

izraz = x*x - (x/x) + 1
print(izraz.expand())
