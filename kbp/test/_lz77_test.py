#
#Kabopan - Readable Algorithms. Public Domain, 2007-2009

from kbp.coder._lz77 import find_longest_match, back_copy

assert find_longest_match("abc","a") == (3, 1)
assert find_longest_match("abc","d") == (0, 0)
assert find_longest_match("abcab","ab") == (2, 2)

assert back_copy("a", 1, 1) == "aa"
assert back_copy("ab", 2, 2) == "abab"
assert back_copy("duplicate me please", 9, 19) == "duplicate me pleaseduplicate"

