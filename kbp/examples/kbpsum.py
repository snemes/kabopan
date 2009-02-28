from getopt import GetoptError, getopt
from sys import argv, exit

__revision__ = "$LastChangedRevision$"
__version__ = '0.1r%d' % int( __revision__.split()[1])
description = "checksum calculator"
  
from kbp.examples.common import get_parameters, makehelp, get_algorithms
  

try:
    import psyco
    psyco.run()
except:
    pass

import kbp.checksum.crc as crc
import kbp.crypt.md2    as md2
import kbp.crypt.md4    as md4
import kbp.crypt.has    as has
import kbp.crypt.sha    as sha
import kbp.crypt.sha2   as sha2
import kbp.crypt.ripemd as ripemd
import kbp.crypt.tiger  as tiger

families = \
{
    "CRCs": \
        {
        "crc32_ieee":["IEEE", crc.crc32_ieee_hexhash,
            "IEEE approved CRC"],
        },
    "HAS": \
        {
        "has160": ["HAS-160", lambda x:has.Has160().compute(x).hexdigest(),
            "Hash Algorithm Standard 160"],
        },
    "MD": \
        {
        "md2":["MD2", lambda x:md2.Md2().compute(x).hexdigest(), ""],
        "md4":["MD4", lambda x:md4.Md4().compute(x).hexdigest(), ""],
        "md5":["MD5", lambda x:md4.Md5().compute(x).hexdigest(), ""],
        },
    "RIPEMD": \
        {
        "ripemd128": ["RIPEMD-128", lambda x:ripemd.Ripemd128().compute(x).hexdigest(), ""],
        "ripemd160": ["RIPEMD-160", lambda x:ripemd.Ripemd160().compute(x).hexdigest(), ""],
        "ripemd256": ["RIPEMD-256", lambda x:ripemd.Ripemd256().compute(x).hexdigest(), ""],
        "ripemd320": ["RIPEMD-320", lambda x:ripemd.Ripemd320().compute(x).hexdigest(), ""],
        },
    "SHA": \
        {
        "sha0": ["SHA-0", lambda x:sha.Sha0().compute(x).hexdigest(), "first SHA algorithm"],
        "sha1": ["SHA-1", lambda x:sha.Sha1().compute(x).hexdigest(), "SHA revision"],
        },
    "SHA-2": \
        {
        "sha224": ["SHA-224", lambda x:sha2.Sha224().compute(x).hexdigest(), ""],
        "sha256": ["SHA-256", lambda x:sha2.Sha256().compute(x).hexdigest(), ""],
        "sha384": ["SHA-384", lambda x:sha2.Sha384().compute(x).hexdigest(), ""],
        "sha512": ["SHA-512", lambda x:sha2.Sha512().compute(x).hexdigest(), ""],
        },
    "tiger": \
        {
        "tiger"   :["tiger-192", lambda x:tiger.Tiger().compute(x).hexdigest(), ""],
        "tiger2"  :["tiger2"   , lambda x:tiger.Tiger2().compute(x).hexdigest(), ""],
        "tiger128":["tiger-128", lambda x:tiger.Tiger128().compute(x).hexdigest(), ""],
        "tiger160":["tiger-160", lambda x:tiger.Tiger160().compute(x).hexdigest(), ""],
        }
    }

algorithms = get_algorithms(families)

Help = makehelp(description, __version__, "<data_to_sum>", families)

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

