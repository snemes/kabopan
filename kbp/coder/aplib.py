#aPLib
#LZSS based lossless compression algorithm
#Jorgen Ibsen, http://www.ibsensoftware.com/
#
#Kabopan - Readable Algorithms. Public Domain, 2009


#todo working but need cleaning and maybe bugfixing

import kbp._bits as _bits
import kbp.coder._lz77 as _lz77

def lengthdelta(offset):
    if offset < 0x80 or 0x7D00 <= offset:
        return 2
    elif 0x500 <= offset:
        return 1
    return 0


class compress(_bits.compress):
    def __init__(self, data, length=None):
        _bits.compress.__init__(self, 1)
        self.__in = data
        self.__length = length if length is not None else len(data)
        self.__offset = 0
        self.__lastoffset = 0
        self.__pair = True
        return

    def __literal(self, marker=True):
        if marker:
            self.write_bit(0)
        self.write_byte(self.__in[self.__offset])
        self.__offset += 1
        self.__pair = True
        return

    def __block(self, offset, length):
        assert offset >= 2
        self.write_bitstring("10")

        # if the last operations were literal or single byte
        # and the offset is unchanged since the last block copy
        # we can just store a 'null' offset and the length
        if self.__pair and self.__lastoffset == offset:
            self.write_variablenumber(2)    # 2-
            self.write_variablenumber(length)
        else:
            high = (offset >> 8) + 2
            if self.__pair:
                high += 1
            self.write_variablenumber(high)
            low = offset & 0xFF
            self.write_byte(low)
            self.write_variablenumber(length - lengthdelta(offset))
        self.__offset += length
        self.__lastoffset = offset
        self.__pair = False
        return

    def __shortblock(self, offset, length):
        assert 2 <= length <= 3
        assert 0 < offset <= 127
        self.write_bitstring("110")
        b = (offset << 1 ) + (length - 2)
        self.write_byte(b)
        self.__offset += length
        self.__lastoffset = offset
        self.__pair = False
        return

    def __singlebyte(self, offset):
        assert 0 <= offset < 16
        self.write_bitstring("111")
        self.write_fixednumber(offset, 4)
        self.__offset += 1
        self.__pair = True
        return

    def __end(self):
        self.write_bitstring("110")
        self.write_byte(chr(0))
        return

    def do(self):
        self.__literal(False)
        while self.__offset < self.__length:
            offset, length = _lz77.find_longest_match(self.__in[:self.__offset],
                self.__in[self.__offset:])
            if length == 0:
                c = self.__in[self.__offset]
                if c == "\x00":
                    self.__windowbyte(0)
                else:
                    self.__literal()
            elif length == 1 and 0 <= offset < 16:
                self.__singlebyte(offset)
            elif 2 <= length <= 3 and 0 < offset <= 127:
                self.__shortblock(offset, length)
            elif 3 <= length and 2 <= offset:
                self.__block(offset, length)
            else:
                self.__literal()
                #raise ValueError("no parsing found", offset, length)
        self.__end()
        return self.getdata()

class decompress(_bits.decompress):
    def __init__(self, data):
        _bits.decompress.__init__(self, data, tagsize=1)
        self.__pair = True    # paired sequence
        self.__lastcopyoffset = 0
        self.__functions = [
            self.__literal,
            self.__block,
            self.__shortblock,
            self.__singlebyte]
        return

    def __literal(self):
        self.read_literal()
        self.__pair = True
        return False

    def __block(self):
        b = self.read_variablenumber()    # 2-
        if b == 2 and self.__pair :    # reuse the same offset
            offset = self.__lastoffset
            length = self.read_variablenumber()    # 2-
        else:
            high = b - 2    # 0-
            if self.__pair:
                high -= 1
            offset = (high << 8) + ord(self.read_byte())
            length = self.read_variablenumber()    # 2-
            length += lengthdelta(offset)
        self.__lastoffset = offset
        self.back_copy(offset, length)
        self.__pair = False
        return False

    def __shortblock(self):
        b = ord(self.read_byte())
        if b <= 1:    # likely 0
            return True
        length = 2 + (b & 0x01)    # 2-3
        offset = b >> 1    # 1-127
        self.back_copy(offset, length)
        self.__lastoffset = offset
        self.__pair = False
        return False

    def __singlebyte(self):
        offset = self.read_fixednumber(4) # 0-15
        if offset:
            self.back_copy(offset)
        else:
            self.read_literal('\x00')
        self.__pair = True
        return False

    def do(self):
        """returns decompressed buffer and consumed bytes counter"""
        self.read_literal()
        while True:
            if self.__functions[self.read_setbits(3)]():
                break
        return self.out, self.getoffset()

if __name__ == "__main__":
    import kbp.test.aplib_test
