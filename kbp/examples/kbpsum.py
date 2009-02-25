from getopt import GetoptError, getopt
from sys import argv, exit

__revision__ = "$LastChangedRevision$"
__version__ = '0.1-%d' % int( __revision__.split()[1])


try:
    import psyco
    psyco.run()
except:
    pass

import kbp.checksum.crc as crc
import kbp.crypt.md2    as md4
import kbp.crypt.md4    as md4
import kbp.crypt.has    as has
import kbp.crypt.sha    as sha
import kbp.crypt.sha2   as sha2
import kbp.crypt.ripemd as ripemd
import kbp.crypt.tiger  as tiger

digesttest = lambda m, s:m.compute(s).hexdigest()

families = [
    "crc", "has", "md", "ripemd", "sha", "tiger", 
    #"adler", "flechter", "gost", "haval", "lm", "panama", "whirlpool", "snefru",
    ]
algorithms = {
    "crc32_ieee":crc.crc32_ieee_hexhash,
    "has-160":lambda x:has.Has160().compute(x).hexdigest(),
    "md2":lambda x:md2.Md2().compute(x).hexdigest(),
    "md4":lambda x:md4.Md4().compute(x).hexdigest(),
    "md5":lambda x:md4.Md5().compute(x).hexdigest(),
    "ripemd-128":lambda x:ripemd.Ripemd128().compute(x).hexdigest(),
    "ripemd-160":lambda x:ripemd.Ripemd160().compute(x).hexdigest(),
    "ripemd-256":lambda x:ripemd.Ripemd256().compute(x).hexdigest(),
    "ripemd-320":lambda x:ripemd.Ripemd320().compute(x).hexdigest(),
    "sha-0"     :lambda x:sha.Sha0().compute(x).hexdigest(),
    "sha-1"     :lambda x:sha.Sha1().compute(x).hexdigest(),
    "sha-224"   :lambda x:sha2.Sha224().compute(x).hexdigest(),
    "sha-256"   :lambda x:sha2.Sha256().compute(x).hexdigest(),
    "sha-384"   :lambda x:sha2.Sha384().compute(x).hexdigest(),
    "sha-512"   :lambda x:sha2.Sha512().compute(x).hexdigest(),
    "tiger"     :lambda x:tiger.Tiger().compute(x).hexdigest(),
    "tiger2"    :lambda x:tiger.Tiger2().compute(x).hexdigest(),
    "tiger128"  :lambda x:tiger.Tiger128().compute(x).hexdigest(),
    "tiger160"  :lambda x:tiger.Tiger160().compute(x).hexdigest(),
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
