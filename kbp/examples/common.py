from getopt import GetoptError, getopt

try:
    import psyco
    psyco.run()
except:
    pass

def makehelp(description, version, parameters, families):
    tab = "   "
    HelpLines = list()
    HelpLines += ["Kabopan %s v%s" % (description, version)]
    HelpLines +=  ["Parameters:  [-a algorithm_keyword] %s" % parameters]
    HelpLines += [""]
    HelpLines += [tab + "input parameters can be a string or a filename."]
    HelpLines += [tab + "each parameter is used as a filename first, then used as a text string if not successful"]
    HelpLines += [""]
    HelpLines += ["Algorithms (families: Name <keyword>: description)"]
    
    for family in sorted(families):
        HelpLines += [tab + "%s:" % family]
        algos = families[family]
        for algo in sorted(algos):
            name, description, function = algos[algo]
            HelpLines += [tab * 2 + "%s <%s> : %s" % (name, algo, description)]
    
    Help = "\n".join(HelpLines)
    return Help

def get_parameters(argv, needed_arguments, algorithms):
    opts = "a:"
    try:
        optlist, args = getopt(argv[1:], opts)
        optlist = dict(optlist)
    
        if "-a" not in optlist:
            requested_algorithms = sorted(algorithms.keys())
        else:
            if optlist["-a"].lower() not in algorithms:
                raise GetoptError("algorithm not found in : "+ " ".join(sorted(algorithms)))
            else:
                requested_algorithms = [optlist["-a"]]
    
    
        if len(args) < needed_arguments:
            raise GetoptError("Not enough arguments")
        else:
            inputs = list()
            for i in xrange(needed_arguments):
                try:
                    with open(args[i], "rb") as f:
                        inputs += [f.read()]
                except IOError:
                    inputs += [args[i]]
    
    except GetoptError, error:
        print("Error: %s\n" % error)
        #print(Help)
        exit()
    return requested_algorithms, inputs

def get_algorithms(families):
    algorithms = dict()
    for f in families.itervalues():
        for a, l in f.iteritems():
            algorithms[a] = l[2]
    return algorithms
