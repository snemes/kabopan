from getopt import GetoptError, getopt
from sys import argv, exit

__version__ = '0.1'
description = "lossless compressor"
  
from kbp.examples.common import get_parameters, makehelp, get_algorithms

families = \
{
    "APLib": \
    {
        "aplib":["APLib", lambda x:x, ""],
    },
    "JCAlg": \
    {
        "jcalg":["JCAlg", lambda x:x, ""],
    },
    "BriefLZ": \
    {
        "brieflz":["BriefLZ", lambda x:x, ""],
    },
}

algorithms = get_algorithms(families)

Help = makehelp(description, __version__, "<data_to_compress>", families)

if len(argv) == 1:
    print(Help)
    exit()

requested_algorithms, inputs = get_parameters(argv, 1, algorithms)
tab = "   "

data_to_sum = inputs[0]
if len(requested_algorithms) == 1:
    print "%s" % (algorithms[requested_algorithms[0]][0](data_to_sum))
else:
    for s in requested_algorithms:
            print "%s%s%s" % (algorithms[s][1], tab, algorithms[s][0](data_to_sum))

