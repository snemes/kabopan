#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from crypt.sha224 import *
from _misc import test_vector_strings

assert [sha224().compute(s).digest() for s in test_vector_strings] == [
    0xd14a028c2a3a2bc9476102bb288234c415a2b01f828ea62ac5b3e42f,
    0xabd37534c7d9a2efb9465de931cd7055ffdb8879563ae98078d6d6d5,
    0x23097d223405d8228642a477bda255b32aadbce4bda0b3f7e36c9da7,
    0x2cb21c83ae2f004de7e81c3c7019cbcb65b71ab656b22d6d0c39b8eb,
    0x45a5f72c39c5cff2522eb3429799e49e5f44b356ef926bcf390dccc2,
    0xbff72b4fcb7d75e5632900ac5f90d219e05e97a7bde72e740db393d9,
    0xb50aecbe4e9bb0b57bc5f3ae760a8e01db24f203fb3cdcd13148046e]
IVs = [
    0xc1059ed8, 0x367cd507, 0x3070dd17, 0xf70e5939, 0xffc00b31, 0x68581511, 0x64f98fa7, 0xbefa4fa4]

class test(sha224):
    def __init__(self):
        sha224.__init__(self)
        assert [int(i) for i in self.IVs] == IVs
test()