#Kabopan - Readable Algorithms. Public Domain, 2009
"""
MD2 - Message Digest 2
Cryptographic hash
The MD2 Message-Digest Algorithm
B. Kaliski, 1992
"""

from kbp._misc import as_bytes_blocks
from kbp._int import BYTES, BYTE
from Hash import merkledamgaard

class md2(merkledamgaard):
    def __init__(self):
        merkledamgaard.__init__(self)
        self.block_length = 16
        self.hv_size = 8
        self.IVs = BYTES([0 for i in xrange(16)])


        # how to calculate this ?
        self.PI_SUBST = [ \
          41, 46, 67, 201, 162, 216, 124, 1, 61, 54, 84, 161, 236, 240, 6,
          19, 98, 167, 5, 243, 192, 199, 115, 140, 152, 147, 43, 217, 188,
          76, 130, 202, 30, 155, 87, 60, 253, 212, 224, 22, 103, 66, 111, 24,
          138, 23, 229, 18, 190, 78, 196, 214, 218, 158, 222, 73, 160, 251,
          245, 142, 187, 47, 238, 122, 169, 104, 121, 145, 21, 178, 7, 63,
          148, 194, 16, 137, 11, 34, 95, 33, 128, 127, 93, 154, 90, 144, 50,
          39, 53, 62, 204, 231, 191, 247, 151, 3, 255, 25, 48, 179, 72, 165,
          181, 209, 215, 94, 146, 42, 172, 86, 170, 198, 79, 184, 56, 210,
          150, 164, 125, 182, 118, 252, 107, 226, 156, 116, 4, 241, 69, 157,
          112, 89, 100, 113, 135, 32, 134, 91, 207, 101, 230, 45, 168, 2, 27,
          96, 37, 173, 174, 176, 185, 246, 28, 70, 97, 105, 52, 64, 126, 15,
          85, 71, 163, 35, 221, 81, 175, 58, 195, 92, 249, 206, 186, 197,
          234, 38, 44, 83, 13, 110, 133, 40, 132, 9, 211, 223, 205, 244, 65,
          129, 77, 82, 106, 220, 55, 200, 108, 193, 171, 250, 36, 225, 123,
          8, 12, 189, 177, 74, 120, 136, 149, 139, 227, 99, 232, 109, 233,
          203, 213, 254, 59, 0, 29, 57, 242, 239, 183, 14, 102, 88, 208, 228,
          166, 119, 114, 248, 235, 117, 75, 10, 49, 68, 80, 180, 143, 237,
          31, 26, 219, 153, 141, 51, 159, 17, 131, 20
        ]

    #todo : merge with Pad, pkcs7 modulo 16 ?
    def padpkcs7(self, length):
        modulo_16 = ((16 - length) % 16)
        padding = modulo_16 if modulo_16 > 0 else 16
        padding_string = chr(padding) * padding
        return padding_string


    def checksum(self, message):
        checksum_bytes = [0 for i in xrange(16)]
        previous = 0
        for block in as_bytes_blocks(message, 16):
            for i,char in enumerate(block):
                # careful, RFC1319 is wrong there. - rfcc209
                # Set C[j] to S[c xor L]
                # should be
                # Set C[j] to (C[j] xor S[c xor L])
                checksum_bytes[i] = checksum_bytes[i] ^ self.PI_SUBST[ord(char) ^ previous]
                previous = checksum_bytes[i]
    
        checksum_string = str().join(chr(i) for i in checksum_bytes)
        return checksum_string

    def pad(self, message):
        padpkcs7 = self.padpkcs7(len(message))
        checksum = self.checksum(message + padpkcs7)
        return padpkcs7 + checksum


    def compute(self, message):
        self.ihvs = list(self.IVs)
        message += self.pad(message)
        block_bytes = [0 for i in xrange(16)]
        xor = BYTES([0 for i in xrange(16)])
        blocks = as_bytes_blocks(message, 16)
    
        for block in blocks:
            block_bytes = [ord(i) for i in block]
            for i in xrange(16):
                xor[i] = self.ihvs[i] ^ block_bytes[i]
    
            previous = BYTE(0)
            for round in xrange(18):
                for l in [self.ihvs, block_bytes, xor]:
                    for k in xrange(16):
                        previous = l[k] = l[k] ^ self.PI_SUBST[previous]
                previous = previous + round
        return self


if __name__ == "__main__":
    import kbp.test.md2_test
