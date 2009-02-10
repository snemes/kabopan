#Mersenne twister: a 623-dimensionally equidistributed uniform pseudorandom number generator
#Makoto Matsumoto and Takuji Nishimura, 1998
#http://www.graviness.com/js/mt19937ar.c.js.phtml
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python


global index, MT
MT = list(range(624 + 1))
index = 0

def init(seed):
    global index, MT
    MT[0] = seed
    for i in range(1, 624 + 1):
        MT[i] = 0xFFFFFFFF & (0x6C078965 * (MT[i - 1] ^ ( (MT[i - 1] >> 30) + i)))


def generate():
    global index, MT
    for i in range(624 + 1):
        y = (0x80000000 & MT[i]) + (0x7FFFFFFF & MT[(i + 1) % 624])
	y &= 0xFFFFFFFF
        MT[i] = MT[(i + 397) % 624] ^ (y >> 1)
        if (y % 2) == 1:
            MT[i] ^= 0x9908b0df


def extract():
    global index, MT
    if index == 0:
        generate()
    y = MT[index]
    y ^= y >> 11
    y ^= (y << 7) & 0x9d2c5680
    y ^= (y << 15) & 0xefc60000
    y ^= y >> 18
    index += 1
    index %= 624
    return y

init(5489)
for i in range(1000):
	print extract()
