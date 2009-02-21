#Ron's Code 4, Rivest's Cipher, RC4, ARC4, ARCFOUR
from kbp.types import BYTE

def init_states(key):
    keylength = len(key)
    states = [BYTE(i) for i in xrange(256)]
    index = BYTE(0)
    for i, dummy in enumerate(states):
        index += states[i] + ord(key[i % keylength])
        states[i], states[index] = states[index], states[i]
    return states


def prga(length, states):
    i = BYTE(0)
    j = BYTE(0)
    for c in xrange(length):
        i += 1
        j += states[i]
        states[i], states[j] = states[j], states[i]
        yield states[states[i] + states[j]]


def crypt(key, message):
    states = init_states(key)
    encrypted = str()
    for char, xor in zip(message, prga(len(message), states)):
        encrypted +=  chr(ord(char) ^ xor)
    return encrypted


if __name__ == "__main__":
    import kbp.test.rc4_test
