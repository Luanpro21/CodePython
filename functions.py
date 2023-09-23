from decimal import*

getcontext().prec = 3

d=Decimal(10)/Decimal(3)
print(d)
print(type(d))

from fractions import*
frac = Fraction(6,9)
print(frac)
print(type(frac))

b = complex(2,5)
print(b)
print(b.real)
print(b.imag)
o=10/6
print(o)
l=2**3
print(l)
p=10%6
print(p)