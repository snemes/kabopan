#Kabopan - Readable Algorithms. Public Domain, 2007-2009

from kbp.crypt.md2 import *
from kbp._misc import test_vector_strings

test_vectors = [
    0x8350E5A3E24C153DF2275C9F80692773,
    0x32EC01EC4A6DAC72C0AB96FB34C0B5D1,
    0xDA853B0D3F88D99B30283A69E6DED6BB,
    0xAB4F496BFB2A530B219FF33031FE06B0,
    0x4E8DDFF3650292AB5A4108C3AA47940B,
    0xDA33DEF2A42DF13975352846C30338CD,
    0xD5976F79D83D3A0DC9806C3C66F3EFD8]

hash = lambda x: md2().compute(x).digest()
assert [hash(s) for s in test_vector_strings] == test_vectors

# in typical MD2 source code, paddings are stored in octal
octal_paddings = [
    "20202020202020202020202020202020",
    "171717171717171717171717171717",
    "1616161616161616161616161616",
    "15151515151515151515151515",
    "141414141414141414141414",
    "1313131313131313131313",
    "12121212121212121212",
    "111111111111111111",
    "1010101010101010",
    "07070707070707",
    "060606060606",
    "0505050505",
    "04040404",
    "030303",
    "0202",
    "01"]

for i in range(32):
    assert octal_paddings[i % 16] == str().join("%02o" % ord(c) for c in md2_u.padpkcs7(i))
