from getopt import *
from sys import argv, exit

import elias, unary, fibonacci


families = {
    "elias":{
        "gamma":elias.gamma_encode,
        "gamma(interleaved)":elias.interleaved_gamma_encode,
        "delta":elias.delta_encode,
        "omega":elias.omega_encode,
        },
    "fibonacci":{
        "fibonacci":fibonacci.encode,
        },
    "unary":{
        "unary":unary.encode,
        },

    }

algorithms = list()
for f in families.itervalues():
    algorithms.extend(list(f.iteritems()))
algorithms = dict(algorithms)


print("Kabopan universal encoder\n")
Help =  "Parameters: [-a algorithm] number\n"
Help += "Algorithms:\n"
for f, algs in families.iteritems():
    Help += "\t%s\n" % f
    for alg in algs:
        Help += "\t\t%s\n" % alg
Help += "\n"

if len(argv) == 1:
    print(Help)
    exit()

opts = "a:"
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
    if len(args) == 0:
        raise GetoptError("missing text or file")
    input = " ".join(args)

except GetoptError, error:
    print("Error: %s\n" % error)
    print(Help)
    exit()

for s in requested_algorithms:
        print "%s\t%s" % (s, algorithms[s](int(input)))
