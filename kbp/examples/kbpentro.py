from getopt import GetoptError, getopt
from sys import argv, exit
from kbp.examples.common import get_parameters, makehelp, get_algorithms

import kbp.entro.huffman    as huffman
import kbp.entro.sfc        as sfc
import kbp.entro._encoding  as encoding

__version__ = '0.1'
description = "entropy encoder"

families = {
    "Huffman":{
        "huffman":["Huffman tree", huffman.generate_tree, ""],
        #"ahuffman":["Adaptative Huffman tree", lambda:str(), "not implemented"],
        },
    "Arithmetic":{
        #"range":["Range Encoding", lambda:str(), "not implemented"],
        #"arithmetic":["Arithmetic Encoding", lambda:str(), "not implemented"],
        },
    "Shannon-Fano":{
        "sfc":["Shannon-Fano coding", sfc.encode, ""]
        }
    }

algorithms = get_algorithms(families)

Help = makehelp(description, __version__, "<data_to_encode>", families)

if len(argv) == 1:
    print(Help)
    exit()

requested_algorithms, inputs = get_parameters(argv, 1, algorithms)
tab = "   "


for s in requested_algorithms:
        print "%s\t%s" % (algorithms[s][1], encoding.generate_codes(algorithms[s][0](inputs[0])))
