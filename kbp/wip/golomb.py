#golomb rice
#entropy encoding
#
#Kabopan - Readable Algorithms. Public Domain, 2007-2009

#preliminary stuff but working

import math

def _b(x, length):
	return bin(x)[2:].rjust(length, '0')

def truncbin(i, b):
	return

def truncbins(n):
	k = int(math.floor(math.log(n,2)))
	b = n - 2 ** k
	#print "n = 2 ** k + b / %(n)i = 2 ** %(k)i + %(b)i" % locals()
	for i in xrange(n):
#		print trunkbin(i, b)
		if i < 2 ** k - b:
			print i, _b(0 + i, k)
		else:
			print i, _b(i + n - 2 * b, k + 1)
	return ""
print truncbins(5)
print truncbins(10)
print truncbins(7)

def unary(n):
	return "0" * n + "1"


def golomb(n, M):
	b = int(math.ceil(math.log(M, 2)))
	q = int(n / M)
#	print n, M, q
	r = n % M
	qb = unary(q)
	if r < 2**b - M:
		rb = _b(r, b - 1)
	else:
		rb = _b(r + 2**b - M, b)
	return " ".join([qb,rb])
def golombs(n, M):
	for i in range(n):
		print golomb(i, M)
golombs(15,4)

