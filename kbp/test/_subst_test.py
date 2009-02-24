#
#Kabopan - Readable Algorithms. Public Domain, 2007-2009

from kbp._subst import *

assert substitute("a", "abcd") == "c"
assert substitute("a", "abcd", lambda x: x + 3) == "d"

assert substitute("ac", "abcd") == "ca"
assert substitute("ac", "abcd", lambda x: x + 3) == "db"

assert mix_alphabet("PLAYFAIR EXAMPLE", "ABCDEFGHIJKLMNOPRSTUVWXYZ") == \
    "PLAYFIREXMBCDGHJKNOSTUVWZ"
 
