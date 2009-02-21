#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
padding functions
"""
def remaining(size, alignment):
    """returns the minimum value to add size to be aligned"""
    return (alignment - (size % alignment)) % alignment


def zero(message, block_length):
    needed = remaining(len(message) * 8, block_length)
    needed /= 8 # this function works with bytes
    return "\x00" * needed


def pkcs7(message, block_length):
    needed = remaining(len(message) * 8, block_length)
    needed /= 8 # this function works with bytes
    return chr(needed) * needed


def bit(message, block_length):
    pad = "\x80"                # 10000000b in hex
    # we just added 8 bits
    needed = remaining(len(message) * 8 + 8, block_length)
    needed /= 8 # working in bytes
    pad += "\x00" * needed
    return pad


def ansix923(message, block_length, length_encoding=32, big_endianness=True):
    needed = (len(message) - length_encoding) % block_length
    needed /= 8 # this function works with bytes
    pad = "\x00" * needed
    pad += pack(length, big_endianness, length_encoding)
    return pad


def iso10126(message, block_length, random=lambda :"\x00",length_encoding=32, big_endianness=True):
    length = len(message)
    needed = (length - (length_encoding / 8)) % block_length
    pad = str()
    for i in needed:
        pad += random()
    pad += pack(length, big_endianness, length_encoding)
    return pad


def pad_0_1_size(message, alignment, sizelength, bigendian):
    """ pads 1 bit, then 0 bits until we have enough bits to store the length of the original message"""
    length = len(message)
    bitlength = length * 8
    padding = "\x80"    # we have to add 1 bit so let's add 0x80 since we're working on byte-boundary block
    current_length = bitlength + 8  # we just added 8 bits
    needed_bits = (alignment - sizelength - current_length) % alignment   # we want to have a block length that
    padding += "\x00" * (needed_bits / 8)
    padding += pack(bitlength, bigendian, sizelength)
    return padding
