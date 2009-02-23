#K abopan - Readable Algorithms. Public Domain, 2009
"""customised standard type classes"""


class Str(str):
    def __init__(self, seq):
            if isinstance(seq, basestring):
                    self.data = seq
            else:
                    self.data = str(seq)

    def __lshift__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        string = self.data
        length = len(string)
        other = other % length
        return self.__class__(string[other:] + string[:other])

    def __rshift__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        string = self.data
        length = len(string)
        other = (length - other) % length
        return self.__class__(string[other:] + string[:other])

    def setstart(self, char):
        """rotate string so that 'char' is the first character"""
        if not isinstance(char, str):
            return NotImplemented
        string = self.data
        if char not in string:
            raise ValueError, "substring not found"
        index = string.index(char)
        return self.__class__(self.__lshift__(index))

    def indexes(self, char):
        if not isinstance(char, str):
            return NotImplemented
        string = self.data
        if char not in string:
            return list()

        result = []
        offset = 0

        while string[offset:].find(char) != -1:
            index = string[offset:].index(char)
            result.append(index + offset)
            offset += index + 1
        return result

    def splitblock(self, block_length):
        if not isinstance(block_length, int):
            return NotImplemented
        string = self.data
        return [self.__class__(string[i: i + block_length]) for i in range(0, len(string), block_length)]

    def insert(self, substring, offset):
        string = self.data
        return self.__class__(string[:offset] + substring + string[offset:])

    def overwrite(self, substring, offset):
        """overwrites 'sub' at 'offset' of 's'"""
        string = self.data
        return self.__class__(string[:offset] + substring + string[offset + len(substring):])


class List(list):
    """list with left and right rotation, as << and >>"""
    def __lshift__(self, other):
        l = len(self)
        limit = other % l
        return List(self[limit:] + self[:limit])

    def __rshift__(self, other):
        l = len(self)
        limit = (l - other) % l
        return List(self[limit:] + self[:limit])

    def __sub__(self, other):
        """returns a List made of other's elements that are not in self, else None"""
        l_diff = lambda x, y: None if x == y else y
        return List(l_diff(x, y) for x, y in zip(self, other))

    def __add__(self, other):
        """returns a list made of 'self' elements if other's is None else other's"""
        l_merge = lambda x, y: x if y == None else y
        return List(l_merge(x, y) for x, y in zip(self, other))

    def replace(self, a, b):
        return List(b if i == a else i for i in self)

#TODO: move to Str ?
def sub_string(a, b):
    """returns a string made of _ if the chars in a and b are the same, else b's"""
    return str().join((List(a) - list(b)).replace(None, "_"))


def add_string(a, d):
    """returns a string made of a char if d's char is '_' else d's char"""
    return str().join(List(a) + List(d).replace("_", None))


class Int():
    """
    integers with limited length encoding, and extra methods
    """
    def __init__(self, number, width):
        self.width = width
        self.modulo = 1 << width
        self.number = int(number) % self.modulo

    def __str__(self):
        return ("%x" % (self.number)).rjust(self.width / 4,"0")

    def __add__(self, other):   return Int((self.number + int(other)) % self.modulo, self.width)
    def __mul__(self, other):   return Int((self.number * int(other)) % self.modulo, self.width)
    def __sub__(self, other):   return Int((self.number - int(other)) % self.modulo, self.width)
    def __div__(self, other):   return Int((self.number / int(other)) % self.modulo, self.width)
    def __xor__(self, other):   return Int((self.number ^ int(other)) % self.modulo, self.width)
    def __or__(self, other):    return Int((self.number | int(other)) % self.modulo, self.width)
    def __and__(self, other):   return Int((self.number & int(other)) % self.modulo, self.width)
    def __mod__(self, other):   return Int((self.number % int(other)) % self.modulo, self.width)
    def __radd__(self, other):  return self.__add__(other)
    def __ror__(self, other):   return self.__or__(other)
    def __rxor__(self, other):   return self.__xor__(other)
    def __rand__(self, other):  return self.__and__(other)
    def __rmod__(self, other):  return self.__mod__(other)
    def __rmul__(self, other):  return self.__mul__(other)

    def __rshift__(self, other):return Int((self.number >> other) % self.modulo, self.width)
    def __lshift__(self, other):return Int((self.number << other) % self.modulo, self.width)

    def __eq__(self, other):    return ((self.number % self.modulo) == other)

    def __invert__(self):      return Int((~self.number) % self.modulo, self.width)
    def __trunc__(self):       return self.number
    def __index__(self):       return self.number
    def rol(self, shift):      return Int(((self.number << shift) | (self.number >> (self.width - shift))) % self.modulo, self.width)
    def ror(self, shift):      return Int(((self.number >> shift) | (self.number << (self.width - shift))) % self.modulo, self.width)

    def endian_swap(self):
        result = 0
        bytewidth = self.width / 8
        for b in range(bytewidth):
            current_byte = (self.number >> ((bytewidth - 1 - b) * 8)) & 0xFF
            result |= current_byte << (b * 8)
        return Int(result, self.width)

    def concat(self, other):
        if not isinstance(other, Int):
            raise TypeError, "Concatting an Int and an int is not supported yet"
        return Int((self.number << other.width) + other.number, self.width + other.width)

    def __getitem__(self, other):
        """extract bytes"""
        if isinstance(other, slice):
            start = 0 if other.start is None else other.start
            stop = self.width / 8 if self.width / 8 < other.stop else other.stop
            return Int(self.number >> (self.width - stop * 8), (stop - start) * 8)
        elif isinstance(other, int):
            shift = other + 1
            return Int(self.number >> (self.width - shift * 8), 8)
        else:
            raise TypeError


class DQWORD(Int):
    def __init__(self, number):
        Int.__init__(self, number, 128)

OWORD = DQWORD

class QWORD(Int):
    def __init__(self, number):
        Int.__init__(self, number, 64)

class DWORD(Int):
    def __init__(self, number):
        Int.__init__(self, number, 32)

class WORD(Int):
    def __init__(self, number):
        Int.__init__(self, number, 16)

class BYTE(Int):
    def __init__(self, number):
        Int.__init__(self, number, 8)


def DWORDS(l):
    return [DWORD(i) for i in l]

def QWORDS(l):
    return [QWORD(i) for i in l]

def BYTES(l):
    return [BYTE(i) for i in l]


if __name__ == "__main__":
    import test.types_test