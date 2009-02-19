#Bellaso cipher (sifra)
#Giovan Battista Bellaso, 1555
#substitution cipher
#
#Kabopan - Readable Algorithms. Public Domain, 2009


from _subst import *
from _str import *
from _misc import *


def first_sifra(data, key):
    """first bellaso substitution cipher"""
    alphabet = "abcdefghilmnopqrstvxyz" # bellaso didn't use a 26 chars alphabet

    constant_part, rotated_part = alphabet[:11], _str(alphabet[11:]) # and it was split in two parts, used differently

    pairs = [alphabet[i:i + 2] for i in range(0, len(alphabet), 2)] #each pair of letters of the key gets a different substitution alphabet
    order = "aeiovcgmqsy" # this is the order of pairs, rotation-wise.

    # now let's generate the substitution alphabet for each pair
    # at each step (following the right order), the rotated part is rotated left one character
    alphabets = dict()
    for index, char in enumerate(order):
        #let's get the pair by its first char in the order
        current_pair = [pair for pair in pairs if char in pair][0]
        alphabets[current_pair] = constant_part + (rotated_part >> index)

    output = str()
    for char, current_key in zip(data, key):
        pair = [p for p in alphabets if current_key in p]
        if pair:
            char = substitute(char, alphabets[pair[0]])
        output += char
    return output


def second_sifra(data, key, alphabet_key):
    #now the substitution alphabet is generated from a passphrase

    consonants = mix_alphabet(alphabet_key, "bcdfghlmnpqrstxyz")
    #then we'll work on the vowels, but we'll insert them every 3 character
    #let's split the consonants string
    consonants_blocks = split_string_blocks(consonants, 3)
    #and parse the key for its used vowels
    vowels = mix_alphabet(alphabet_key, "aeiou")
    #let's merge the consonants and vowels data

    alphabet = "".join(i + j for i, j in zip_extend(consonants_blocks, list(vowels)))

    #assert alphabet == "rmqacntupsbidfgehlxoyz"
    constant_part, rotated_part = alphabet[:11], _str(alphabet[11:])

    #now to generate the pairs, we'll do the same, but merge the vowel every char blocks
    consonants_blocks = split_string_blocks(consonants, 1)
    pairs_string = _str("".join(i + j for i, j in zip_extend(consonants_blocks, list(vowels))))
    pairs = pairs_string.splitblock(2)

    #now we have the pairs, the initial substitution alphabet
    #let's generate the 'rotated' alphabet for each pair
    alphabets = dict()
    for index, pair in enumerate(pairs):
        #let's get the pair by its first char in the order
        alphabets[pair] = constant_part + (rotated_part >> index)

    # now the actual encryption
    # for this cipher, the xth character of the key is used to decrypt the xth word (space separated) of the plaintext
    output = str()
    key_index = 0
    for char  in data:
        pair = [p for p in alphabets if key[key_index] in p]
        if pair:
            char = substitute(char, alphabets[pair[0]])
        if char == ' ':
            key_index += 1
        output += char
    return output

#not enough information for his autokey cipher

if __name__ == "__main__":
    import test.bellaso_test