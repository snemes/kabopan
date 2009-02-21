#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
Uuencode format
"""
import base
from kbp._misc import char_range

LENGTHS = "`" + char_range(chr(33), chr(33 + 45 - 1)) # 0 is encoded as `, the other char starting from 33"
UUENCODE = char_range(" ", "_").replace(" ", "`")


def encode(filename):
    with open(filename,"rt") as f:
        r = f.read()
        mode = "644"
        print "begin " + mode + " " + filename
        encoded = base.encode(r, base.base256, UUENCODE)
        blocks = (encoded[i: i + 60] for i in range(0,  len(encoded), 60))
        for block in blocks:
            print LENGTHS[len(block) * 3 / 4] + block

        print LENGTHS[0] + ""
        print "end"


def decode(filename):
    with open(filename,"rt") as f:
        r = f.read()
        lines = r.splitlines()
        filename = lines[0][10:]
        print filename
        data = str()
        for line in lines[1:]:
            length = (LENGTHS.index(line[0]) & 63) * 4 / 3
            if length == 0:
                break
            data += line[1:]
        print data
        decoded = base.decode(data, base.base256, UUENCODE)
        print decoded

#import sys
#filename = sys.argv[1]
#decode(filename)