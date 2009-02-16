from getopt import *
from sys import argv, exit

__revision__ = "$LastChangedRevision$"
__version__ = '0.1-%d' % int( __revision__.split()[1])


try:
    import psyco
    psyco.run()
except:
    pass

import checksum.crc
import crypt.md2
import crypt.md4
import crypt.has
import crypt.sha
import crypt.sha2
import crypt.ripemd
import crypt.tiger

digesttest = lambda m, s:m.compute(s).hexdigest()

families = [
    "crc", "has", "md", "ripemd", "sha", "tiger", 
    #"adler", "flechter", "gost", "haval", "lm", "panama", "whirlpool", "snefru",
    ]
algorithms = {
    "crc32_ieee":checksum.crc.crc32_ieee_hexhash,
    "has-160":lambda x:crypt.has.has160().compute(x).hexdigest(),
    "md2":lambda x:crypt.md2.md2().compute(x).hexdigest(),
    "md4":lambda x:crypt.md4.md4().compute(x).hexdigest(),
    "md5":lambda x:crypt.md4.md5().compute(x).hexdigest(),
    "ripemd-128":lambda x:crypt.ripemd.ripemd128().compute(x).hexdigest(),
    "ripemd-160":lambda x:crypt.ripemd.ripemd160().compute(x).hexdigest(),
    "ripemd-256":lambda x:crypt.ripemd.ripemd256().compute(x).hexdigest(),
    "ripemd-320":lambda x:crypt.ripemd.ripemd320().compute(x).hexdigest(),
    "sha-0"     :lambda x:crypt.sha.sha0().compute(x).hexdigest(),
    "sha-1"     :lambda x:crypt.sha.sha1().compute(x).hexdigest(),
    "sha-224"   :lambda x:crypt.sha2.sha224().compute(x).hexdigest(),
    "sha-256"   :lambda x:crypt.sha2.sha256().compute(x).hexdigest(),
    "sha-384"   :lambda x:crypt.sha2.sha384().compute(x).hexdigest(),
    "sha-512"   :lambda x:crypt.sha2.sha512().compute(x).hexdigest(),
    "tiger"     :lambda x:crypt.tiger.tiger().compute(x).hexdigest(),
    "tiger2"    :lambda x:crypt.tiger.tiger2().compute(x).hexdigest(),
    "tiger128"  :lambda x:crypt.tiger.tiger128().compute(x).hexdigest(),
    "tiger160"  :lambda x:crypt.tiger.tiger160().compute(x).hexdigest(),
    #"adler32":_,
    #"flechter16":_,
    #"flechter32":_,
    #"gost":_,
    #"haval":_,
    #"panama":_,
    #"lm":_,
    #"snefru":_,
    #"whirlpool":_,
    }
Help = "Kabopan checksum calculator\n"
Help +=  "Parameters:  [-a algorithm] <[-f <input file>]|[<text>]>\n"
Help += "Algorithms:\n\t"+ "\n\t".join([", ".join([a for a in sorted(algorithms) if a.startswith(f)]) for f in families])

if len(argv) == 1:
    print(Help)
    exit()

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

if len(requested_algorithms) == 1:
    print "%s" % (algorithms[requested_algorithms[0]](input))
else:
    for s in requested_algorithms:
            print "%s\t%s" % (s, algorithms[s](input))
