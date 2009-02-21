#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
Ascii85 / Base85
base coder
Paul E. Rutter
"""

from kbp._misc import ASCII, DIGITS, ALPHABET, ALPHABET_LOWERCASE, char_range
from kbp._subst import substitute


ASCII85_1924  = DIGITS + ALPHABET + ALPHABET_LOWERCASE +  "!#$%&()*+-;<=>?@^_`{|}~" # for reference only, for RFC 1924

ASCII85 = char_range(chr(33), chr(33 + 85 - 1))


def merge(number_list, base):
    result = 0
    for i in number_list:
        result = result * base + i

    return result


def split(number, base, max_digits=0):
    result = list()
    digits = 0
    remainder = number
    while remainder != 0:
            number = remainder % base
            remainder /= base
            digits += 1
            result = [number] + result
    if digits < max_digits:
        result = [0 for i in range (max_digits - digits)] + result
    return result


def encode(source):
    # todo : starter/ender and y/z belong to the format, not the algo
    tetragrams = (source[i:i + 4] for i in range(0, len(source), 4))
    result = ""
    result += "<~"
    for l in tetragrams:
        if l == "    ":
            result += "y"   # instead of "+<VdL"
        elif l == "\x00\x00\x00\x00":
            result += "z"   # instead of "!!!!!"
        else:
            length = len(l)
            if length < 4:
                l =  l + '\x00' * (4 - length)
            value = merge ([ASCII.index(i) for i in l], len(ASCII))
            l = split(value, len(ASCII85), 5)[:length + 1]
            result += "".join(ASCII85[i] for i in l)
    result = result + "~>"
    return result


def decode(target):
    target = target[2:-2]
    target = target.replace("y", "+<VdL")
    target = target.replace("z", "!!!!!")
    result = str()
    pentagrams = (target[i:i + 5] for i in range(0, len(target), 5))
    for l in pentagrams:
        length = len(l)
        if length < 5:
            l += "u" * (5 - length)
        value = merge((ASCII85.index(i) for i in l), len(ASCII85))
        encoded_char = 4
        l = split(value, len(ASCII), 4)[:length - 1]

        result += "".join((ASCII[i] for i in l))
    return result

if __name__ == "__main__":
    import kbp.test.ascii85_test
