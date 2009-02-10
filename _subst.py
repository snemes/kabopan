#useful functions for substitution ciphers
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from _misc import *

def substitute(original, alphabet, substitution=None):
    """substitute all characters in 'original' that are present in 'alphabet'
    according to the 'substitution' function.
    
    if no 'substitution' function is provided, it is done on rotating 
    on half the alphabet length, so that it's reciprocal"""
    if substitution is None:
        substitution = lambda x:x + len(alphabet) / 2

    substituted = str()
    for char in original:
        if char in alphabet:
            character_index = alphabet.index(char)
            new_index = substitution(character_index) % len(alphabet)
            substituted_char = alphabet[new_index]
            substituted += substituted_char
        else:
            substituted += char
    return substituted



def mix_alphabet(key_string, alphabet):
    """mix alphabet by ordering them by their order of first appearance in the key,
    if not present then by their alphabet order"""

    # mixed_alphabet = "".join(sorted(alphabet, key = (key_string + alphabet).index)) # one liner :)
    remaining_letters = list(alphabet)
    mixed_alphabet = str()
    for char in key_string:
            if char in remaining_letters:
                    remaining_letters.remove(char)
                    mixed_alphabet += char
    mixed_alphabet += "".join(remaining_letters)

    return mixed_alphabet


if __name__ == "__main__":
    import _subst_test