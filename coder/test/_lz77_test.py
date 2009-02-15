#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from coder._lz77 import *

assert find_longest_match("abc","a") == (3,1)
assert find_longest_match("abc","d") == (0,0)
assert find_longest_match("abcab","ab") == (2,2)

assert back_copy("a",1,1) == "aa"
assert back_copy("ab",2,2) == "abab"
assert back_copy("duplicate me please",9,19) == "duplicate me pleaseduplicate"

