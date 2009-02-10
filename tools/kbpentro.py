from getopt import *
from sys import argv, exit

import huffman, sfc, _encoding

families = {
    "huffman":{
        "huffman":huffman.generate_tree,
        },
    "shannon-fano":{
        "sfc":sfc.encode,
        }
    }

algorithms = list()
for f in families.itervalues():
    algorithms.extend(list(f.iteritems()))
algorithms = dict(algorithms)


print("Kabopan entropy encoder\n")
Help =  "Parameters:  [-a algorithm] <[-f <input file>]|[<text>]>\n"
Help += "Algorithms:\n"
for f, algs in families.iteritems():
    Help += "\t%s\n" % f
    for alg in algs:
        Help += "\t\t%s\n" % alg
Help += "\n"


opts = "a:f:"
try:
    optlist, args = getopt(argv[1:], opts)
    optlist = dict(optlist)

    if "-a" not in optlist:
        requested_algorithms = sorted(algorithms.keys())
    else:
        if optlist["-a"] not in algorithms:
            raise GetoptError("algorithm not found")
        else:
            requested_algorithms = [optlist["-a"]]
    if len(args) == 0 and "-f" not in optlist:
        raise GetoptError("missing text or file")

    if "-f" in optlist:
        with open(optlist["-f"], "rb") as f:
            input = f.read()
    else:
        input = " ".join(args)

except GetoptError, error:
    print("Error: %s\n" % error)
    print(Help)
    exit()

for s in requested_algorithms:
        print "%s\t%s" % (s, _encoding.generate_codes(algorithms[s](input)))
