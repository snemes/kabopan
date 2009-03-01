#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
RC4, ARC4, ARCFOUR, Ron's Code 4, Rivest's Cipher 4
"""
from kbp.types import Byte

def init_states(key):
    """init rc4 state"""
    keylength = len(key)
    states = [Byte(i) for i in xrange(256)]
    index = Byte(0)
    for i, dummy in enumerate(states):
        index += states[i] + ord(key[i % keylength])
        states[i], states[index] = states[index], states[i]
    return states


def prga(length, states):
    """generate 'length' prn from 'states'"""
    i = Byte(0)
    j = Byte(0)
    for c in xrange(length):
        i += 1
        j += states[i]
        states[i], states[j] = states[j], states[i]
        yield states[states[i] + states[j]]


def crypt(key, message):
    """
    encrypt/decrypt 'message' from 'key'
    
    @param key: key for en/de-cryption
    @param message: plain/cipher-text to be en/de-crypted
    @return: cipher/plain-text"""
    states = init_states(key)
    encrypted = str()
    for char, xor in zip(message, prga(len(message), states)):
        encrypted +=  chr(ord(char) ^ xor)
    return encrypted


if __name__ == "__main__":
    import kbp.test.rc4_test
