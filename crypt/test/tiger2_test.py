#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from crypt.tiger2 import *
from _misc import test_vector_strings, ass
import sys

test_vectors = [
    0x4441BE75F6018773C206C22745374B924AA8313FEF919F41,
    0x67E6AE8E9E968999F70A23E72AEAA9251CBC7C78A7916636,
    0xF68D7BC5AF4B43A06E048D7829560D4A9415658BB0B1F3BF,
    0xE29419A1B5FA259DE8005E7DE75078EA81A542EF2552462D,
    0xF5B6B6A78C405C8547E91CD8624CB8BE83FC804A474488FD,
    0xEA9AB6228CEE7B51B77544FCA6066C8CBB5BBAE6319505CD,
    0xD85278115329EBAA0EEC85ECDC5396FDA8AA3A5820942FFF]

ass(test_vectors, [tiger2().compute(s).digest() for s in test_vector_strings], "test vectors")