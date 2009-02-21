#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
cryptographic hash
HAVAL --- a one-way hashing algorithm with variable length of output
Yuliang Zheng, Josef Pieprzyk, Jennifer Seberry 1992
http://labs.calyptix.com/haval.php
"""


# collision, XiaoyunWang, Dengguo Feng, Xuejia Lai, Hongbo Yu, 2004
"""
collision, as dwords...
6377448b d9e59f18 f2aa3cbb d6cb92ba ee544a44 879fa576 1ca34633 76ca5d4f
a67a8a42 8d3adc8b b6e3d814 5630998d 86ea5dcd a739ae7b 54fd8e32 acbb2b36
38183c9a b67a9289 c47299b2 27039ee5 dd555e14 839018d8 aabbd9c9 d78fc632
fff4b3a7 40000096 7f466aac fffffbc0 5f4016d2 5f4016d0   12e2b0 f4307f87

6377488b d9e59f18 f2aa3cbb d6cb92ba ee544a44 879fa576 1ca34633 76ca5d4f
a67a8a42 8d3adc8b b6e3d814 d630998d 86ea5dcd a739ae7b 54fd8e32 acbb2b36
38183c9a b67a9289 c47299ba 27039ee5 dd555e14 839018d8 aabbd9c9 d78fc632
fff4b3a7 40000096 7f466aac fffffbc0 5f4016d2 5f4016d0   12e2b0 f4307f87"""

#from fractions import Fraction
#from mpmath import *
#mp.dps = 50
#from fractions import *
#getcontext().prec=2000
#p = Fraction(0)
#for i in range(1000):
#	p += Fraction(4*((-1)**i), 2*i+1)
#print Decimal(p.numerator)/Decimal(p.denominator)
#4*(-1)**n/(2*n+1)
#from sympy import *
#_1310_digits_of_float_part_of_pi_in_hex = 
#print "%x" % int((pi.evalf(n=2000) - 3)* 2 ** (32 * 136))

from kbp._pickle import get_variables, save_variables
from kbp.types import DWORD
from decimal import Decimal, getcontext

pickled = get_variables("haval", ["K"])
if pickled is None:
    import decimal
    decimal.getcontext().prec=1320

    #Pi decimals via leibniz formula
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    pi = 0
    while len(str(pi)) < 1320:
        
        # Next approximation
        p, q, k = k*k, 2*k+1, k+1
        a, b, a1, b1 = a1, b1, p*a+q*a1, p*b+q*b1
        # Print common digits
        d = a / b
        d1 = a1 / b1
        while d == d1:
            pi = pi * 10 + d
            a, a1 = 10*(a%b), 10*(a1%b1)
            d, d1 = a/b, a1/b1
    float_pi = decimal.Decimal("0."+ str(pi)[1:]) 

    all_K = []
    for i in xrange(136):
        float_pi = (float_pi * 2 ** 32)% (2 ** 32)
        all_K += [DWORD(int(float_pi))]
    
    lower = 0
    
    K = []
    for l in (1,4,4,4,4):
        length = l * 8
        K += [all_K[lower: lower + length]]
        lower += length

    save_variables("haval", {"K":K})
else:
    K = pickled["K"]
