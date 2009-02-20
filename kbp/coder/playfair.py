#Kabopan - Readable Algorithms. Public Domain, 2009
"""
Playfair cipher/square
Charles Wheatstone, 1854
substitution cipher
"""

from kbp._misc import insert_string, split_string_blocks
from kbp._subst import substitute, mix_alphabet

ALPHABET25 = "ABCDEFGHIJKLMNOPRSTUVWXYZ" # no Q
ALPHABET25_NOJ = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # no J, alternative possibility

def get_coordinates(square, char):
    index = square.index(char)
    row = index / 5
    column = index % 5
    return row, column

def get_char(square, row, column):
    char = square [column + row * 5]
    return char

def encode(plaintext, key):
    square = mix_alphabet(key, ALPHABET25)
    plaintext = plaintext.replace(" ","").upper()
    #let's split the plaintext in digraph, while inserting X to avoid single letter digraphs
    i = 0
    digraphs = list()
    while i < len(plaintext) - 1:
        if i == len(plaintext) - 1: # wrong if last char is X
            plaintext = insert_string(plaintext, i + 1, 'X')
        elif i < len(plaintext) - 1 and plaintext[i] == plaintext[i + 1]:
            plaintext = insert_string(plaintext, i + 1, 'X')
        digraphs += [plaintext[i:i + 2]]
        i += 2

    ciphertext = str()
    for digraph in digraphs:
        #get both chars, their coordinates
        char1, char2 = list(digraph)
        row1, column1 = get_coordinates(square, char1)
        row2, column2 = get_coordinates(square, char2)
        encoded_row1, encoded_column1 = row1, column1
        encoded_row2, encoded_column2 = row2, column2

        #apply transformation rules
        if row1 != row2 and column1 != column2: # making a rectangle - take the other 2 corners, with the same row respectively
            encoded_row1, encoded_column1 = row1, column2
            encoded_row2, encoded_column2 = row2, column1
        elif row1 != row2 and column1 == column2: # same column - get the caracter down
            encoded_row1 = (row1 + 1) % 5
            encoded_row2 = (row2 + 1) % 5
        elif row1 == row2 and column1 != column2: # same row - get the caracter right
            encoded_column1 = (column1 + 1) % 5
            encoded_column2 = (column2 + 1) % 5

        #output resulting chars
        encoded_char1 = get_char(square, encoded_row1, encoded_column1)
        encoded_char2 = get_char(square, encoded_row2, encoded_column2)
        ciphertext += encoded_char1 + encoded_char2

    return ciphertext


def decode(ciphertext, key):
    square = mix_alphabet(key, ALPHABET25)
    digraphs = split_string_blocks(ciphertext, 2)

    plaintext = str()
    for digraph in digraphs:
        #get both chars, their coordinates
        char1, char2 = list(digraph)
        row1, column1 = get_coordinates(square, char1)
        row2, column2 = get_coordinates(square, char2)
        encoded_row1, encoded_column1 = row1, column1
        encoded_row2, encoded_column2 = row2, column2

        #apply transformation rules
        if row1 != row2 and column1 != column2: # making a rectangle - take the other 2 corners, with the same row respectively
            encoded_row1, encoded_column1 = row1, column2
            encoded_row2, encoded_column2 = row2, column1
        elif row1 != row2 and column1 == column2: # same column - get the caracter up
            encoded_row1 = (row1 - 1) % 5
            encoded_row2 = (row2 - 1) % 5
        elif row1 == row2 and column1 != column2: # same row - get the caracter left
            encoded_column1 = (column1 - 1) % 5
            encoded_column2 = (column2 - 1) % 5

        #output resulting chars
        encoded_char1 = get_char(square, encoded_row1, encoded_column1)
        encoded_char2 = get_char(square, encoded_row2, encoded_column2)
        plaintext += encoded_char1 + encoded_char2

    return plaintext


if __name__ == "__main__":
    import kbp.test.playfair_test
