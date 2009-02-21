#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
vigenere cipher, substitution cipher

Blaise de Vigenere, 1586
"""

from kbp._misc import ALPHABET, ALPHABET_LOWERCASE
from kbp._subst import substitute

def vigenere(plaintext, key):
    ciphertext = str()
    for (char, current_key) in zip(plaintext, key):
        current_shift = ALPHABET.index(current_key)
        shifted_char = substitute(char, ALPHABET, lambda x: x + current_shift)
        shifted_char = substitute(shifted_char, ALPHABET_LOWERCASE, lambda x: x + current_shift)
        ciphertext += shifted_char
    return ciphertext


if __name__ == "__main__":
    import kbp.test.vigenere_test
