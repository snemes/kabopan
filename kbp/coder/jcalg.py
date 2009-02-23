#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
JCALG1, LZSS based lossless compression algorithm

Jeremy Collake U{http://www.bitsum.com}
"""

#compress not working yet

from kbp._bits import compress, decompress
import kbp.coder._lz77

def lengthdelta(x):
    if x >= 0x10000:
        return  3;
    elif x >= 0x37FF:
        return 2;
    elif x >= 0x27F:
        return 1;
    elif x <= 127:
        return 4;
    return 0

class compress(compress):
    """not working correctly yet"""
    def __init__(self, data, length=None):
        compress.__init__(self, 4)
        self.__in = data
        self.__length = length if length is not None else len(data)
        self.__lastindex = 1
        self.__indexbase = 8
        self.__literalbits = 0
        self.__literaloffset = 0
        self.__offset = 0
        return

    def __literal(self):
        self.write_bit(0)
        self.write_fixednumber(ord(self.__in[self.__offset]) - self.__literaloffset, self.__literalbits)
        self.__ofset += 1
        return

    def __block(self, offset, length):
        assert offset >= 2
        if offset == self.__lastindex:
            self.write_variablenumber(2)
            self.write_variablenumber(length)
        else:
            #tbc
            print("not working yet")
            pass
        self.writebitstr("10")
        return

    def __shortblock(self, offset, length):
        self.write_bitstring("110")
        return

    def __nullliteral(self):
        self.write_bitstring("110")
        self.write_fixednumber(1, 4)
        self.__ofset += 1
        return

    def __singlebyte(self, offset):
        assert 0 <= offset < 16
        self.write_bitstring("111")
        self.write_fixednumber(offset, 4)
        self.__offset += 1
        self.__pair = True
        return

    def __updateindexbase(self, value):
        self.writebitstr("111")
        self.write_fixednumber(0, 7)
        nb = misc.countbits(value)
        self.write_fixednumber(value, nb - 3)

    def __end(self):
        self.write_bitstr("111")
        self.write_fixednumber(0, 7)
        self.write_fixednumber(0, 2)
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



class decompress(decompress):
    """jcalg decompression class"""
    def __init__(self, data):
        decompress.__init__(self, data, tagsize=4)
        self.__lastindex = 1
        self.__indexbase = 8
        self.__literalbits = 0
        self.__literaloffset = 0
        self.__functions = [
            self.__literal,
            self.__normalphrase,
            self.__onebyteorliteralchange,
            self.__shortmatch,
            ]
        return

    def __literal(self):
        # literal
        self.read_literal(chr(self.read_fixednumber(self.__literalbits)
             + self.__literaloffset))
        return False

    def __normalphrase(self):
        # dictionary copy with same or new offset
        HighIndex = self.read_variablenumber()

        if (HighIndex == 2):
            # use the last index
            length = self.read_variablenumber();
        else:
            self.__lastindex = ((HighIndex - 3) << self.__indexbase) \
                + self.read_fixednumber(self.__indexbase);
            length = self.read_variablenumber();
            length += lengthdelta(self.__lastindex)
        self.back_copy(self.__lastindex, length)
        return False


    def __onebyteorliteralchange(self):
        onebytephrasevalue = self.read_fixednumber(4) - 1
        if onebytephrasevalue == 0:

            # null literal
            self.read_literal("\0x00")
        else:
            if onebytephrasevalue > 0:

                # single byte
                self.back_copy(onebytephrasevalue)
            else:

                if self.read_bit():

                    # 256 * 8 bit blocks until readbit
                    for i in xrange(256):
                        self.out += self.read_fixednumber(8)
                    while self.read_bit():
                        for i in xrange(256):
                            self.out += self.read_fixednumber(8)
                else:

                    # new literal size
                    self.__literalbits = 7 + self.read_bit()
                    self.__literaloffset = 0
                    if self.__literalbits != 8:
                        self.__literaloffset = self.read_fixednumber(8)
        return False

    def __shortmatch(self):
        # shortmatch, end or indexbase update
        newindex = self.read_fixednumber(7)
        matchlength = 2 + self.read_fixednumber(2)
        if newindex == 0:
            if matchlength == 2:

                # end
                return True

            #indexbase update
            self.__indexbase = self.read_fixednumber(matchlength + 1)
        else:

            #short block
            self.__lastindex = newindex
            self.back_copy(self.__lastindex, matchlength)
        return False

    def do(self):
        """returns decompressed buffer and consumed bytes counter"""
        while True:
            if self.__functions[self.read_setbits(3, 0)]():
                break
        return self.out, self.getoffset()
