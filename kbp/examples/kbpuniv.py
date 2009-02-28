from getopt import GetoptError, getopt
from sys import argv, exit
from kbp.examples.common import get_parameters, makehelp, get_algorithms

import kbp.univ.elias     as elias
import kbp.univ.unary     as unary
import kbp.univ.fibonacci as fibonacci

__version__ = '0.1'
description = "universal encoder"

families = {
    "elias":{
        "gamma":["Gamma encoding", elias.gamma_encode, ""],
        "gamma-2":["interleaved Gamma", elias.interleaved_gamma_encode,
            "Gamma with length and value encoded together, very efficient"],
        "delta":["Delta encoding", elias.delta_encode, ""],
        "omega":["Omega encoding", elias.omega_encode, ""],
        },
    "fibonacci":{
        "fibonacci":["Fibonacci encoding", fibonacci.encode,
            "decomposition in fibonacci numbers, and their index unary encoded"],
        },
    "unary":{
        "unary":["Unary encoding", unary.encode,
            "the simplest and less efficient encoding"],
        },

    }

algorithms = get_algorithms(families)

Help = makehelp(description, __version__, "<number_to_encode>", families)

if len(argv) == 1:
    print(Help)
    exit()

requested_algorithms, inputs = get_parameters(argv, 1, algorithms)
tab = "   "

for s in requested_algorithms:
        print "%s\t%s" % (algorithms[s][1], algorithms[s][0](int(inputs[0])))
