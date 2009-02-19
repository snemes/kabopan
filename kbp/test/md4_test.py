#Kabopan - Readable Algorithms. Public Domain, 2009
"""tests for MD4 and MD5"""

from kbp._misc import rol, hex2bin, test_vector_strings
from kbp.crypt.md4 import *
from kbp._int import *

hashmd4 = lambda x: md4().compute(x).digest()

md4_IVs = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

md4_test_vectors = [
    0x31d6cfe0d16ae931b73c59d7e0c089c0,
    0xbde52cb31de33e46245e05fbdbd6fb24,
    0xa448017aaf21d8525fc10ae87aa6729d,
    0xd9130a8164549fe818874806e1c7014b,
    0xd79e1c308aa5bbcdeea8ed63df412da9,
    0x043f8582f241db351ce627e153e7f0e4,
    0xe33b4ddc9c38f2199c3e7b164fcc0536]

# collision, XiaoyunWang, Dengguo Feng, Xuejia Lai, Hongbo Yu, 2004

a4 = \
 "839c7a4d 7a92cb56 78a5d5b9 eea5a757 3c8a74de b366c3dc 20a083b6 9f5d2a3b"\
 "b3719dc6 9891e9f9 5e809fd7 e8b23ba6 318edd45 e51fe397 08bf9427 e9c3e8b9"

delta4 = \
 "_______________d________2______________________________________________"\
 "_________________________________________c_____________________________"

b4 = add_string(a4, delta4)
b4 = b4.replace(" ","")
a4, b4 = [hex2bin(s) for s in [a4, b4]]



ass(md4_u.IVs, md4_IVs, "md4 IVs")
ass(md4_test_vectors, [hashmd4(s) for s in test_vector_strings], "md4 test vectors")
assert hashmd4(a4) == hashmd4(b4)

# MD5
hashmd5 = lambda x: md5().compute(x).digest()

md5_test_vectors = [
    0xd41d8cd98f00b204e9800998ecf8427e,
    0x0cc175b9c0f1b6a831c399e269772661,
    0x900150983cd24fb0d6963f7d28e17f72,
    0xf96b697d7cb7938d525a2f31aaf161d0,
    0xc3fcd3d76192e4007dfb496cca67e13b,
    0xd174ab98d277d9f5a5611c2c9f419d9f,
    0x57edf4a22be3c955ac49da2e2107b67a]

# collision, XiaoyunWang, Dengguo Feng, Xuejia Lai, Hongbo Yu, 2004
a5 = \
 "d131dd02c5e6eec4693d9a0698aff95c 2fcab58712467eab4004583eb8fb7f89"\
 "55ad340609f4b30283e488832571415a 085125e8f7cdc99fd91dbdf280373c5b"\
 "d8823e3156348f5bae6dacd436c919c6 dd53e2b487da03fd02396306d248cda0"\
 "e99f33420f577ee8ce54b67080a80d1e c69821bcb6a8839396f9652b6ff72a70"

delta5 = \
 "_______________________________________0_________________________"\
 "__________________________f____________________________7_________"\
 "_______________________________________3_________________________"\
 "__________________________2____________________________a_________"

b5 = add_string(a5, delta5)
md5_a, md5_b = [hex2bin("".join(s).replace(" ", "")) for s in [a5, b5]]


ass(md5_test_vectors, [hashmd5(s) for s in test_vector_strings], "md5 test vectors")
assert hashmd5(md5_a) == hashmd5(md5_b)


#EXTRA, obsolete
#md4 round parameters usual representation
md4_rounds = [
    'A BCD 00 03 f 0x00000000',
    'D ABC 01 07 f 0x00000000',
    'C DAB 02 11 f 0x00000000',
    'B CDA 03 19 f 0x00000000',
    'A BCD 04 03 f 0x00000000',
    'D ABC 05 07 f 0x00000000',
    'C DAB 06 11 f 0x00000000',
    'B CDA 07 19 f 0x00000000',
    'A BCD 08 03 f 0x00000000',
    'D ABC 09 07 f 0x00000000',
    'C DAB 10 11 f 0x00000000',
    'B CDA 11 19 f 0x00000000',
    'A BCD 12 03 f 0x00000000',
    'D ABC 13 07 f 0x00000000',
    'C DAB 14 11 f 0x00000000',
    'B CDA 15 19 f 0x00000000',
    'A BCD 00 03 g 0x5A827999',
    'D ABC 04 05 g 0x5A827999',
    'C DAB 08 09 g 0x5A827999',
    'B CDA 12 13 g 0x5A827999',
    'A BCD 01 03 g 0x5A827999',
    'D ABC 05 05 g 0x5A827999',
    'C DAB 09 09 g 0x5A827999',
    'B CDA 13 13 g 0x5A827999',
    'A BCD 02 03 g 0x5A827999',
    'D ABC 06 05 g 0x5A827999',
    'C DAB 10 09 g 0x5A827999',
    'B CDA 14 13 g 0x5A827999',
    'A BCD 03 03 g 0x5A827999',
    'D ABC 07 05 g 0x5A827999',
    'C DAB 11 09 g 0x5A827999',
    'B CDA 15 13 g 0x5A827999',
    'A BCD 00 03 h 0x6ED9EBA1',
    'D ABC 08 09 h 0x6ED9EBA1',
    'C DAB 04 11 h 0x6ED9EBA1',
    'B CDA 12 15 h 0x6ED9EBA1',
    'A BCD 02 03 h 0x6ED9EBA1',
    'D ABC 10 09 h 0x6ED9EBA1',
    'C DAB 06 11 h 0x6ED9EBA1',
    'B CDA 14 15 h 0x6ED9EBA1',
    'A BCD 01 03 h 0x6ED9EBA1',
    'D ABC 09 09 h 0x6ED9EBA1',
    'C DAB 05 11 h 0x6ED9EBA1',
    'B CDA 13 15 h 0x6ED9EBA1',
    'A BCD 03 03 h 0x6ED9EBA1',
    'D ABC 11 09 h 0x6ED9EBA1',
    'C DAB 07 11 h 0x6ED9EBA1',
    'B CDA 15 15 h 0x6ED9EBA1']

#s = "%s %s%s%s %02i %02i %s 0x%08X" % (ABCD[a], ABCD[b], ABCD[c], ABCD[d], k, s, f.__name__, constant)


#md5 round parameters usual representation
md5_rounds = [
 [ 7, "f",  0, 0xD76AA478],
 [12, "f",  1, 0xE8C7B756],
 [17, "f",  2, 0x242070DB],
 [22, "f",  3, 0xC1BDCEEE],
 [ 7, "f",  4, 0xF57C0FAF],
 [12, "f",  5, 0x4787C62A],
 [17, "f",  6, 0xA8304613],
 [22, "f",  7, 0xFD469501],
 [ 7, "f",  8, 0x698098D8],
 [12, "f",  9, 0x8B44F7AF],
 [17, "f", 10, 0xFFFF5BB1],
 [22, "f", 11, 0x895CD7BE],
 [ 7, "f", 12, 0x6B901122],
 [12, "f", 13, 0xFD987193],
 [17, "f", 14, 0xA679438E],
 [22, "f", 15, 0x49B40821],
 [ 5, "g",  1, 0xF61E2562],
 [ 9, "g",  6, 0xC040B340],
 [14, "g", 11, 0x265E5A51],
 [20, "g",  0, 0xE9B6C7AA],
 [ 5, "g",  5, 0xD62F105D],
 [ 9, "g", 10, 0x02441453],
 [14, "g", 15, 0xD8A1E681],
 [20, "g",  4, 0xE7D3FBC8],
 [ 5, "g",  9, 0x21E1CDE6],
 [ 9, "g", 14, 0xC33707D6],
 [14, "g",  3, 0xF4D50D87],
 [20, "g",  8, 0x455A14ED],
 [ 5, "g", 13, 0xA9E3E905],
 [ 9, "g",  2, 0xFCEFA3F8],
 [14, "g",  7, 0x676F02D9],
 [20, "g", 12, 0x8D2A4C8A],
 [ 4, "h",  5, 0xFFFA3942],
 [11, "h",  8, 0x8771F681],
 [16, "h", 11, 0x6D9D6122],
 [23, "h", 14, 0xFDE5380C],
 [ 4, "h",  1, 0xA4BEEA44],
 [11, "h",  4, 0x4BDECFA9],
 [16, "h",  7, 0xF6BB4B60],
 [23, "h", 10, 0xBEBFBC70],
 [ 4, "h", 13, 0x289B7EC6],
 [11, "h",  0, 0xEAA127FA],
 [16, "h",  3, 0xD4EF3085],
 [23, "h",  6, 0x04881D05],
 [ 4, "h",  9, 0xD9D4D039],
 [11, "h", 12, 0xE6DB99E5],
 [16, "h", 15, 0x1FA27CF8],
 [23, "h",  2, 0xC4AC5665],
 [ 6, "i",  0, 0xF4292244],
 [10, "i",  7, 0x432AFF97],
 [15, "i", 14, 0xAB9423A7],
 [21, "i",  5, 0xFC93A039],
 [ 6, "i", 12, 0x655B59C3],
 [10, "i",  3, 0x8F0CCC92],
 [15, "i", 10, 0xFFEFF47D],
 [21, "i",  1, 0x85845DD1],
 [ 6, "i",  8, 0x6FA87E4F],
 [10, "i", 15, 0xFE2CE6E0],
 [15, "i",  6, 0xA3014314],
 [21, "i", 13, 0x4E0811A1],
 [ 6, "i",  4, 0xF7537E82],
 [10, "i", 11, 0xBD3AF235],
 [15, "i", 02, 0x2AD7D2BB],
 [21, "i",  9, 0xEB86D391]
]
