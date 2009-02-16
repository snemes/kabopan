#
#Kabopan - Readable Algorithms. Public Domain, 2009

from transf.mtf import *

assert move_to_front([0, 1, 2, 3, 4], 2) == [2, 0, 1, 3, 4]
assert move_to_front([0, 1, 2, 3, 4], 3) == [3, 0, 1, 2, 4]

assert transform("caraab") == [2, 1, 3, 1, 0, 3]

assert revert(["a", "b", "c", "r"],[2, 1, 3, 1, 0, 3]) == "caraab"

