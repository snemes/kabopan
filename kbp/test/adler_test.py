#Kabopan - Readable Algorithms. Public Domain, 2007-2009
from kbp.checksum.adler import adler32


assert adler32("abracadabra") == 0x19F20455