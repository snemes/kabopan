from _int import *

class Feistel:
    def __init__(self):
        self.rounds = 0
        self.middle = 0
        self.in_f = lambda x, y: x ^ y
        self.out_f = self.in_f

    def round_parameters(self, backward):
        pass

    def crypt(self, plaintext, key):
        L = DWORD(0) # plaintext[:self.middle]
        R = DWORD(0) # plaintext[self.middle:]
        for F, extra in self.round_parameters(backward=False):
            L, R = R, self.in_f(L, F(R, key, *extra))
        return L, R

    def decrypt(self, ciphertext, key):
        #L = ciphertext[:self.middle]
        #R = ciphertext[self.middle:]
        #L, R = DWORDS([0x41ea3a0a, 0x94baa940]) 
        L, R = DWORDS([0xdee9d4d8, 0xf7131ed9]) # for xtea
        for F, extra in self.round_parameters(backward=True):
            L, R = self.out_f(R, F(L, key, *extra)), L
        return L, R


