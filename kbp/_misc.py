#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
various functions for binary calculations, display...
"""
#todo : a lot of cleaning is likely required

from kbp.types import Int
import struct

def char_range(start, end):
    """returns a list of char from 'start' to 'end'"""
    return "".join(chr(i) for i in range(ord(start), ord(end) + 1))

LITTLE, BIG = False, True
DIGITS = char_range("0", "9")
ALPHABET = char_range("A", "Z")
ALPHABET_LOWERCASE = char_range("a", "z")
ASCII = char_range("\x00", "\xff")

def gcd(a, b):
    """returns the greatest common divisor of both parameters"""
    return gcd(b, a % b) if b != 0 else a

def lcm(a, b):
    """returns the least common multiplier of both parameters"""
    return a * b / gcd(a, b)

def getbinlen(value):
    """return the bit length of an integer"""
    result = 0
    if value == 0:
        return 1
    while value != 0:
        value >>= 1
        result += 1
    return result

def getlongestcommon(a, b):
    """returns i, maximum value such that a[:i] == b[:i]"""
    l = min(len(i) for i in  [a, b])
    res = 0
    while res < l and a[res] == b[res]:
        res += 1
    return res


def gethyphenstr(s, limit = 9, sep = " [...] "):
    """turns a long string into a [...]-shortened string"""
    if len(s) > 2*limit + len(sep):
        return s[:limit].rstrip() + sep + s[-limit:].lstrip()
    else:
        return s


def getbinstr(value):
    """return the smallest binary representation of an integer"""
    if value == 0:
        return "0"

    result = ""
    while value != 0:
        if value & 1:
            result = "1" + result
        else:
            result = "0" + result
        value >>= 1
    return result


def getvaluefrombinarystring(string):
    """return the value from a binary string"""
    result = 0
    for char in string:
        bit = 1 if char == "1" else 0
        result = (result << 1) + bit
    return result


def countmissing(value, modulo):
    """returns x > 0 so that (value + x) % modulo = 0 (useful to write leading zeroes)"""
    result = value % modulo
    if result == 0:
        result = modulo
    return modulo - result

def getpadbinstr(value, bits):
    """return a 0-padded binary string."""
    s = getbinstr(value)
    l = len(s)
    mod = countmissing(l, bits)
    return "0" * mod + s


def getunkbinstr(value, currentbit, maxbit):
    """returns a binary string representation of the command/tag

    including unset bits, according to currentbit.
    it displays 'value' as a binary string, padded according to 'maxbit',
    then hides the lowest bits until 'currentbit'"

    """
    s = getpadbinstr(value, maxbit + 1)[:maxbit - currentbit + 1]
    mod = countmissing(len(s), maxbit + 1)
    return s + "x" * mod



def gethexstr(string):
    """convert a string to its hex equivalent"""
    return " ".join("%02X" % (ord(char)) for char in string)



def int2lebin(value, size):
    """ouputs value in binary, as little-endian"""
    result = ""
    for i in xrange(size):
        result = result + chr((value >> (8 * i)) & 0xFF )
    return result


def int2bebin(value, size):
    """ouputs value in binary, as big-endian"""
    result = ""
    for i in xrange(size):
        result = chr((value >> (8 * i)) & 0xFF ) + result
    return result


def md5(s):
    """returns hex digest of the md5 of the string"""
    import hashlib
    return hashlib.md5(s).hexdigest()



def modifystring(s, sub, offset):
    """overwrites 'sub' at 'offset' of 's'"""
    return s[:offset] + sub + s[offset + len(sub):]


#todo : sort what's next
def brutting_snippet(data, function):
    """
    1. run unpacking code on all offsets,
    2. store consumed bits
    3. remembers the biggest one
    """
    maxlen = 0
    result = {}
    for i in xrange(50):
        blz = function(data[i:])
        decomp, consumed = blz.do()
        maxlen = max(len(decomp), maxlen)
        result[len(decomp)] = i
        print

    print result
    print maxlen, result[maxlen]
    return result[maxlen]

def write_snippet(filename, data):
    """simple write file snippet"""
    f = open(filename + ".out", "wb")
    for i in data:
        f.write(i)
    f.close()

def checkfindest(dic, stream, offset, length):
    """checks that findlongeststring result is correct"""
    temp = dic[:]
    for i in xrange(length):
        temp += temp[-offset]
    if temp != dic + stream[:length]:
        print temp
        print dic + stream[:length]
        return False
    return True

def insert_string(string, offset, char):
    """insert a char in a string"""
    return string[:offset] + char + string[offset:]



def zip_extend(a, b, null=""):
    """zip 2 sequences after extending the smallest with null elements"""
    if len(a) == len(b):
        return zip(a, b)

    smaller = a if len(a) < len(b) else b
    bigger = a if len(a) > len(b) else b
    max_length = max(len(i) for i in (a, b))
    smaller.extend([null] * (max_length - len(smaller)))
    return zip(bigger, smaller)


def zip_extend_str(a, b, null=""):
    """zip string by padding the shortest one with 'null' char"""
    a = list(a)
    b = list(b)
    return zip_extend(a, b, null)

def split_string_blocks(string, block_length):
    """returns a list of blocks made of block_length length"""
    return [string[i: i + block_length] for i in range(0, len(string), block_length)]


def rorstr(string, count=1):
    """rotate right"""
    length = len(string)
    count = (length - count) % length

    result = string[count:] + string[:count]
    return result

def setstr(string, index):
    """rotate string until the 'index' char is the first one"""
    rot = string
    for i in xrange(len(string)):
        rot = rorstr(rot)
        if rot[0] == index:
            return rot
    return

test_vector_strings = [
    "",
    "a",
    "abc",
    "message digest",
    "abcdefghijklmnopqrstuvwxyz",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
    "1234567890" * 8]

MASK = dict([i, (1 << i) - 1] for i in [8, 16, 32, 64])

#TODO: obsoleted by Int ?
def rol(number, shift, width=32):
    """left rotation"""
    number &= MASK[width]
    result = ((number << shift) | (number >> (width - shift))) & ((1 << width) - 1)
    result &= MASK[width]
    return result

def rol32(n, s):
    """DWORD left rotation"""
    return rol(n, s, 32)
def rol64(n, s):
    """QWORD left rotation"""
    return rol(n, s, 64)


#TODO: obsoleted by Int ?
def ror(number, shift, width):
    """right rotation"""
    return rol(number, (width - shift) % width, width)

def ror32(n, s):
    """DWORD ror """
    return ror(n, s, 32)
def ror64(n, s):
    """QWORD ror """
    return ror(n, s, 64)


#TODO: obsoleted by Int ?
def split_number(number, bits, amount, bigendian=False):
    """split a number made of 'bits' bits in a list of numbers, taking bits separately"""
    result = list()
    mask = (1 << bits) - 1
    for i in range(amount):
        value = ( number >> ((amount - 1 - i) * bits)) & mask
        if not bigendian:
            value = byteswap(value, 4)
        result.append(value)
    return result

#TODO: obsoleted by Int ?
def merge_number(numbers, bigendian=False, bits=32):
    """merge a list of number as a bigger number"""
    result = 0
    for index, number in enumerate(numbers[::-1]):
        value = number if bigendian else byteswap(number, bits / 8)
        result += (int(value) << (bits * index))
    return result

#TODO: obsoleted by Int ?
def byteswap(number, bytesize):
    """endian-swap a number"""
    result = 0
    for b in range(bytesize):
        current_byte = (number >> ((bytesize - 1 - b) * 8)) & 0xFF
        result |= current_byte << (b * 8)
    return result


#TODO: obsoleted by Int ?
def nibbleswap(number, bytesize):
    """swap every nibble of a number"""
    result = 0
    for b in range(bytesize):
        current_byte = (number >> (b * 8)) & 0xFF
        current_byte =  ((current_byte & 0xF) << 4) | ((current_byte & 0xF0) >> 4)
        result |= current_byte << (b * 8)
    return result

def xor(gen, start = 0):
    """xor all elements of 'gen', from 'start'"""
    result = start
    for i in gen:
        result ^= i
    return result

from decimal import Decimal

def nroot(integer, n):
    """returns n-root via Decimal module """
    return Decimal(integer) ** (Decimal(1) / Decimal(n))

def generate_primes(last_prime):
    """generate consecutive primes, until last_prime. inefficient, just working"""
    result = range(2, last_prime + 1)
    for i in xrange(2, last_prime):
        for j in result:
            if j != i and j % i == 0:
                result.remove(j)
    return result


def frac(i):
    """returns fractional part"""
    return i % 1


def hsqrt(i):
    """hex representation of square root of i"""
    return int(2 ** 30 * i ** (1. / 2))


def hcbrt(i):
    """hex representation of cube root of i"""
    return int(2 ** 30 * i ** (1. / 3))

import traceback, sys
def ass(x, y, msg=None, details=False):
    """cleaner assert"""
    try:
        assert x == y, msg
    except AssertionError, msg:
        f, n, _t, l = traceback.extract_stack()[0]
        f = f[f.rindex("\\") + 1:]
        print "%s(%i): Error %s : %s" % (f, n, msg, l)
        from pprint import pprint
        if details:
            pprint(x)
            pprint(y)
        sys.exit()

def add(out_, in_, width):
    """add with masking. obsolete? """
    for i, j in enumerate(out_):
        out_[i] += in_[i]
        out_[i] &= MASK[width]
    return out_ # unneeded if we didn't do a shallow copy of out_

struct_prefixes = {True:">", False:"<"}
struct_sizes = {32:"L", 64:"Q"}

def pack128(number, bigendian=False):
    """pack on OQWORDS"""
    struct_string = struct_prefixes[bigendian] + struct_sizes[64]
    if bigendian:
        return struct.pack(struct_string, number >> 64) + struct.pack(struct_string, number)
    else:
        return struct.pack(struct_string, number) + struct.pack(struct_string, number >> 64)

def pack64(number, bigendian=False):
    """pack on QWORD"""
    return struct.pack(struct_prefixes[bigendian] + struct_sizes[64], number)

def pack32(number, bigendian=False):
    """pack on DWORDs"""
    return struct.pack(struct_prefixes[bigendian] + struct_sizes[32], number)

def pack(number, bigendian, width):
    """returns a dictionary of packing functions"""
    return {32:pack32, 64:pack64, 128:pack128}[width](number, bigendian)

def pad_0_1_size(message, alignment, sizelength, bigendian, pad_bit_7):
    """ pads 1 bit, then 0 bits until we have enough bits to store the length of the original message"""
    pad_char = {True:"\x80", False: "\x01"}[pad_bit_7]
    length = len(message)
    bitlength = length * 8
    padding = pad_char    # we have to add 1 bit so let's add 0x80 since we're working on byte-boundary block
    current_length = bitlength + 8  # we just added 8 bits
    needed_bits = (alignment - sizelength - current_length) % alignment   # we want to have a block length that
    padding += "\x00" * (needed_bits / 8)
    padding += pack(bitlength, bigendian, sizelength)
    return padding

def as_words(block, block_size, word_size, bigendian=False):
    """split a string as words by unpacking"""
    count_ = block_size / word_size
    unpack_string = struct_prefixes[bigendian] + str(count_) + struct_sizes[word_size]
    return [Int(i, word_size) for i in list(struct.unpack(unpack_string, block))]



def as_bytes_blocks(s, x):
    """slices s in 'x' blocks """
    return (s[i: i + x] for i in xrange(0, len(s), x))

def simplepad(message):
    """simple padding"""
    last_block = len(message) % 4
    pad = "1"
    if last_block  == 3:
        return [pad, "extr"]
    else:
        return [pad + "_" * (3 - last_block)]

    return

def slice_and_pad(message, x, pad=simplepad):
    """generate slices of the message, then pad the last block"""
    length = len(message)
    # div is the number of complete blocks
    # last_block_length is 0 if all blocksmod is the length of the last block if it's too short
    complete_blocks, last_block_length = divmod(length, x)
    for block in (message[i: i + x] for i in xrange(0, complete_blocks * x, x)):
        yield block
    padding = pad(message)  #

    if last_block_length > 0:
        last_block = message[-last_block_length:]
        yield last_block + padding[0]
        for block in padding[1:]:
            yield block
    else:
        for block in padding:
            yield block
    return


def hex2bin(s):
    """takes a hexadecimal string, returns the binary equivalent"""
    result = str()
    s = s.replace(" ","")
    HEXA = "0123456789ABCDEF"
    for b in as_bytes_blocks(s, 2):
        result += chr( HEXA.index(b[0].upper()) * 16 + HEXA.index(b[1].upper()))
    return result

def bin2hex(s):
    """takes a hex string, return the equivalent number"""
    result = str()
    HEXA = "0123456789ABCDEF"
    for b in s:
        b = ord(b)
        result += HEXA[b >> 4] + HEXA[b & 0xF]
    return result

#TODO obsolete
def printh(l):
    """print in hex"""
    print ["%x" % i for i in l]

if __name__ == "__main__":
    import kbp.test._misc_test
