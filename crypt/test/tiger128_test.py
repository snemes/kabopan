#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from crypt.tiger128 import *
from _misc import test_vector_strings, ass

test_vectors = [
    0x3293ac630c13f0245f92bbb1766e1616,
    0x77befbef2e7ef8ab2ec8f93bf587a7fc,
    0x2aab1484e8c158f2bfb8c5ff41b57a52,
    0xd981f8cb78201a950dcf3048751e441c,
    0x1714a472eee57d30040412bfcc55032a,
    0x8dcea680a17583ee502ba38a3c368651,
    0x1c14795529fd9f207a958f84c52f11e8]


ass(test_vectors, [tiger128().compute(s).digest() for s in test_vector_strings], "test vectors")
