#Kabopan - Readable Algorithms. Public Domain, 2009

from checksum.fletcher import *


def get_adler_limit():
    return max(n for n in xrange(2 ** (32 / 2)) if (255 * n * (n + 1)/2 + (n + 1) * (65521 - 1) <= 2 ** 32 - 1))


def adler32(data_to_checksum):
    return compute(data_to_checksum, 32, 65521, limit=5552)

if __name__ == "__main__":
    import test.adler_test