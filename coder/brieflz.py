#BriefLZ
#LZSS-based compression algorithm
#Jorgen Ibsen, http://www.ibsensoftware.com/
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python


#TODO working, but need cleaning and bugfixing

import _bits
import _lz77

debug = False


class compress(_bits.compress):
    def __init__(self, data, length=None):
        _bits.compress.__init__(self, 2)
        self.__in = data
        self.__length = length if length is not None else len(data)
        self.__offset = 0

    def __literal(self):
        self.write_bit(0)
        self.write_byte(self.__in[self.__offset])
        self.__offset += 1
        return

    def __dictcopy(self, offset, length):
        assert offset >= 1
        assert length >= 4
        
        self.write_bit(1)
        self.write_variablenumber(length - 2)
        value = offset - 1
        high = ((value >> 8) & 0xFF) + 2    # 2-257
        low = value & 0xFF
        self.write_variablenumber(high)  # 2-
        self.write_byte(chr(low))    # 0-255
        self.__offset += length
        return

    def do(self):
        self.write_byte(self.__in[self.__offset])
        self.__offset += 1
        while self.__offset < self.__length:
            offset, length = _lz77.find_longest_match(self.__in[:self.__offset],
                self.__in[self.__offset:])
            if offset >= 1 and length >= 4:
                self.__dictcopy(offset, length)
            else:
                self.__literal()
        return self.getdata()


class decompress(_bits.decompress):
    def __init__(self, data, length=None):
        _bits.decompress.__init__(self, data, 2)
        if length is None:
            length = len(data)
        # brieflz specific
        self.length = length
        self.__functions = [
            self.read_literal,
            self.__dictcopy
            ]
        return

    def __dictcopy(self):
        length = self.read_variablenumber() + 2
        high = self.read_variablenumber() - 2
        low = ord(self.read_byte())
        offset = (high << 8) + low + 1
        self.back_copy(offset, length)
        return

    def do(self):
        """returns decompressed buffer and consumed bytes counter"""
        self.read_literal()
        while self.getoffset() < self.length:
            self.__functions[self.read_setbits(1)]()
        return self.out, self.getoffset()


if __name__ == "__main__":
    import test.brieflz_test
