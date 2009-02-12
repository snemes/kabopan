#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from _misc import rol, hex2bin, test_vector_strings
from crypt.md4 import *

hash = lambda x: md5().compute(x).digest()

test_vectors = [
    0xd41d8cd98f00b204e9800998ecf8427e,
    0x0cc175b9c0f1b6a831c399e269772661,
    0x900150983cd24fb0d6963f7d28e17f72,
    0xf96b697d7cb7938d525a2f31aaf161d0,
    0xc3fcd3d76192e4007dfb496cca67e13b,
    0xd174ab98d277d9f5a5611c2c9f419d9f,
    0x57edf4a22be3c955ac49da2e2107b67a]

assert [hash(s) for s in test_vector_strings] == test_vectors


# let's check results of our round parameters generator
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

# collision, XiaoyunWang, Dengguo Feng, Xuejia Lai, Hongbo Yu, 2004

a = [
"d131dd02c5e6eec4693d9a0698aff95c 2fcab58712467eab4004583eb8fb7f89",
"55ad340609f4b30283e488832571415a 085125e8f7cdc99fd91dbdf280373c5b",
"d8823e3156348f5bae6dacd436c919c6 dd53e2b487da03fd02396306d248cda0",
"e99f33420f577ee8ce54b67080a80d1e c69821bcb6a8839396f9652b6ff72a70"]

b = [
"d131dd02c5e6eec4693d9a0698aff95c 2fcab50712467eab4004583eb8fb7f89",
"55ad340609f4b30283e4888325f1415a 085125e8f7cdc99fd91dbd7280373c5b",
"d8823e3156348f5bae6dacd436c919c6 dd53e23487da03fd02396306d248cda0",
"e99f33420f577ee8ce54b67080280d1e c69821bcb6a8839396f965ab6ff72a70"]

a, b = [hex2bin("".join(s).replace(" ", "")) for s in [a, b]]

assert hash(a) == hash(b)

class test(md5):
    def __init__(self):
        md5.__init__(self)

        rounds = list()
        for self.round in range(4): 
            function = self.round_parameters()
            for self.iteration in range(16):
                shift, k, g = self.iteration_parameters()
                rounds.append([shift, function.__name__, g, k])
        
        assert md5_rounds == rounds

test()
