#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
ROT5 / ROT13 / ROT18 / ROT47 / Caesar
substitution cipher
"""

from kbp._subst import substitute
from kbp._misc import char_range, DIGITS, ALPHABET, ALPHABET_LOWERCASE

ASCII33_126 = char_range("!", "~")

def rot5(data):
    return substitute(data, DIGITS)

def rot13(data):
    return substitute(substitute(data, ALPHABET), ALPHABET_LOWERCASE)

def rot18(data):
    return rot13(rot8(data))

def rot47(data):
    return substitute(data, ASCII33_126)

def caesar_encode(plaintext):
    return substitute(plaintext, ALPHABET, lambda x: x + 3)

def caesar_decode(ciphertext):
    return substitute(ciphertext, ALPHABET, lambda x: x - 3)

if __name__ == "__main__":
    import kbp.test.rot_test
