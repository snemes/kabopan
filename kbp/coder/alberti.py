#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
Alberti cipher (disk) / Captain Midnight Decoder Badge

substitution cipher
De Cifris
Leone Battista Alberti
1467
"""

from kbp._misc import setstr
from kbp._subst import substitute

from random import randrange
DISK1 ="ABCDEFGILMNOPQRSTVXZ1234" # uppercase, stationary, plaintext
DISK2 ="gklnprtuz&xysomqihfdbace" # lowercase, mobile, cyphertext
NUMBERS = "1234"

# two disks. align them to a start position.
# read the plaintext on the outer, uppercase disk, get the ciphertext on the inner disk.

def switch_alphabet(source, target, char):
    position = source.index(char)
    return target[position]


def encrypt_mode1(plaintext, start_position, change_index=None):
# in this mode, at anytime, the position can be changed
# when it happens, output the outer disk's character that is aligned with the inner disk's starting position

    current_disk1 = DISK1   # this disk is fixed but used for on-the-fly index change so it's relatively turning
    current_disk2 = setstr(DISK2, start_position) # let's turn the disk to the right index

    ciphertext = str()
    for i, char in enumerate(plaintext):
        if char in DISK1:
            ciphertext += switch_alphabet(current_disk1, current_disk2, char)
        if change_index and i % change_index == change_index - 1: # time to change position
            new_position = current_disk1[randrange(len(current_disk2))]
            ciphertext += new_position

            current_disk1 = setstr(current_disk1, new_position)
    return ciphertext


def decrypt_mode1(ciphertext, start_position):
    plaintext = str()
    current_disk1 = DISK1
    current_disk2 = setstr(DISK2, start_position) # let's turn the disk to the right index
    for char in ciphertext:
        if char in DISK1:
            current_disk1 = setstr(DISK1, char)
        else:
            decoded_char = switch_alphabet(current_disk2, current_disk1, char)
            if decoded_char not in NUMBERS: # numbers are discarded during decryption
                plaintext += decoded_char
    return plaintext


# mode 2: in this mode, the disks are realigned <=> an extra character of a number (1-4) is inserted in the plaintext
# the encoded char will be used as index

def encrypt_mode2(plaintext, start_position):
    current_disk1 = DISK1   # this disk is fixed but used for on-the-fly index change so it's relatively turning
    current_disk2 = setstr(DISK2, start_position) # let's turn the disk to the right index
    ciphertext = str()
    for char in plaintext:
        encoded_char = switch_alphabet(current_disk1, current_disk2, char)
        ciphertext += encoded_char
        if char in NUMBERS:
            current_disk2 = setstr(current_disk2, encoded_char)
    return ciphertext


def decrypt_mode2(plaintext, start_position):
    current_disk1 = DISK1
    current_disk2 = setstr(DISK2, start_position)
    ciphertext = str()
    for char in plaintext:
        decoded_char = switch_alphabet(current_disk2, current_disk1, char)
        if decoded_char in NUMBERS:
            current_disk2 = setstr(current_disk2, char)
        else:
            ciphertext += decoded_char
    return ciphertext


if __name__ == "__main__":
    import kbp.test.alberti_test