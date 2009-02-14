#Kabopan - Readable Algorithms. Public Domain, 2009
"""customised standard type classes"""
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


def _test():
    assert List([1,2,3,4]) >> 1 == [4, 1,2,3]
    assert List([1,2,3,4]) >> 4 == [1,2,3,4]
    assert List([1,2,3,4]) << 1 == [2,3,4, 1]

    assert 0xFFCD9AD6 == DWORD(251972843051734)
    assert 0x9AD6 == WORD(251972843051734)
    assert 0xD6 == BYTE(251972843051734)
    assert str(QWORD(17)) == "0000000000000011"
    assert 214 == BYTE(251972843051734)
    assert BYTE(15 + 1)  == BYTE(15) + 1

    # casting is important
    assert BYTE(0xF) + DWORD(0xFFFFF00) == 0xF
    assert DWORD(0xFFFFF00) + BYTE(0xF) == 0xFFFFF0F
    assert DWORD(BYTE(0xF)) + DWORD(0xFFFFF00) == 0xFFFFF0F
    assert int(BYTE(0xF)) + DWORD(0xFFFFF00) == 0xFFFFF0F
    assert DQWORD(0xF) == OWORD(0xE) + 1

    i = DWORD(0x4345669)
    assert i[:3].concat(i[3:]) == i

if __name__ == "__main__":
    _test()