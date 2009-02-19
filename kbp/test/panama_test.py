#Kabopan - Readable Algorithms. Public Domain, 2009

from kbp.crypt.panama import *
from kbp._misc import test_vector_strings

test_vectors = [
        0xaa0cc954d757d7ac7779ca3342334ca471abd47d5952ac91ed837ecd5b16922b,
        0x6604ca6420aeb684418846d02a9005a57477c8decd46bdbdfaf0c8e23be268fd,
        0xa2a70386b81fb918be17f00ff3e3b376a0462c4dc2eec7f2c63202c8874c037d,
        0x6d0ad9e9844386add2101aabdb85dfe253e518a10aa7507b863735b999fae5e8,
        0xcbf13b835674785f6a5741276be2384397187ff12a8a6652a1a1549b14507130,
        0x4aeff66cd896d63e03ac2f98a36e8a73f7de5faba470e7901d84e3d555f59da6,
        0x1325a194745de0560ecb0bcc2f0de0f4f626157873e3fe1987a8080fba0220bf]

#assert test_vectors == [hash(s) for s in test_vector_strings], "panama test vectors"
