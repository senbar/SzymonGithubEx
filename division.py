#NIE DZIALA XD
from polyUnit import *
from translate import *
poly = Translate(input("Input polynomial: "))
div = Translate(input("Input divisor: "))
def Division(poly,div):
    quo = polyUnit()
    t = polyUnit()
    rem = polyUnit()
    rem.exponent = poly.exponent
    rem.factor = poly.factor
    i = 0
    while rem != 0 and rem[-1].exponent >= div[-1].exponent:
        i += 1
        t[0].exponent = rem[-1].exponent - div[-1].exponent
        t[0].factor = rem[-1].factor / div[-1].factor
        quo[-i].exponent = t[0].exponent
        quo[-i].factor = t[0].factor
        rem[-1].exponent = rem.exponent - i
        rem[-i].factor = rem.factor - t[0].factor * div[-i].factor
    return(quo,rem)
    print(quo[-1].factor)
    print(quo[-1].exponent)

    #print(t.exponent)
    #print(poly[1].factor)
