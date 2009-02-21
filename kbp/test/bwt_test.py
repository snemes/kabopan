#Kabopan - Readable Algorithms. Public Domain, 2007-2009

from kbp.transf.bwt import *

assert transform('abraca') == ('caraab', 1)


assert get_indexes('abcaba','a') == [0, 3, 5]
assert get_indexes('abcaba','d') == []


assert rotate_string("abc", 1) == "bca"
assert rotate_string("abc", 2) == "cab"


assert revert(*transform('abraca')) == 'abraca'
test = "The quick brown fox jumps over the lazy dog"
assert test == revert(*transform(test))
assert transform(test) == ('kynxesergl i hhv otTu c uwd rfm ebp qjoooza', 8)
