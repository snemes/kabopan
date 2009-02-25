#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
classes for variable-sized auto-reloading tag, sliding window, compression and decompression algorithms
"""


#todo : working, but needs a lot of cleaning, and bugfixing

import kbp._misc as _misc

debug = False

def bits(string, bit7_first=True):
    for char in string:
        char_value = ord(char)
        for current_bit in range(8):
            #by default, we read the most significant bit first
            bit_index = 7 - current_bit if bit7_first else current_bit
            boolean = ((char_value & (1 <<  bit_index)) != 0)

            yield boolean


def reverse(integer, width):
    reversed_ = 0
    for i in range(width):
        reversed_ |= ((integer >> i) & 1) << (width - 1 - i)
    return reversed_


class compress:
    """bit machine for variable-sized auto-reloading tag compression"""
    def __init__(self, tagsize):
        """tagsize is the number of bytes that takes the tag"""
        self.out = ""

        self.__tagsize = tagsize
        self.__tag = 0
        self.__tagoffset = -1
        self.__maxbit = (self.__tagsize * 8) - 1
        self.__curbit = 0
        self.__isfirsttag = True


    def getdata(self):
        """builds an output string of what's currently compressed:
        currently output bit + current tag content"""
        tagstr = _misc.int2lebin(self.__tag, self.__tagsize)
        return _misc.modifystring(self.out, tagstr, self.__tagoffset)

    def write_bit(self, value):
        """writes a bit, make space for the tag if necessary"""
        if self.__curbit != 0:
            self.__curbit -= 1
        else:
            if self.__isfirsttag:
                self.__isfirsttag = False
            else:
                self.out = self.getdata()
            self.__tagoffset = len(self.out)
            self.out += "".join(["\x00"] * self.__tagsize)
            self.__curbit = self.__maxbit
            self.__tag = 0

        if value:
            self.__tag |= (1 << self.__curbit)
        return

    def write_bitstring(self, s):
        """write a string of bits"""
        for c in s:
            self.write_bit(0 if c == "0" else 1)
        return

    def write_byte(self, b):
        """writes a char or a number"""
        assert len(b) == 1 if isinstance(b, str) else 0 <= b <= 255
        self.out += b[0:1] if isinstance(b, str) else chr(b)
        return

    def write_fixednumber(self, value, nbbit):
        """write a value on a fixed range of bits"""
        for i in xrange(nbbit - 1, -1, -1):
            self.write_bit( (value >> i) & 1)
        return

    def write_variablenumber(self, value):
        assert value >= 2

        length = _misc.getbinlen(value) - 2 # the highest bit is 1
        self.write_bit(value & (1 << length))
        for i in xrange(length - 1, -1, -1):
            self.write_bit(1)
            self.write_bit(value & (1 << i))
        self.write_bit(0)
        return



# unused debug visual stuff

#    def getstatus(self):
#        return "status " + " / ".join([
#            gethyphenstr(gethexstr(self.bsdata[:self.tagoffset])) ,
#            self.getunkbinstr(self.tag, self.currentbit, self.maxbit) + " %0X" % (self.tag),
#            gethexstr(self.bsdata[self.tagoffset + self.tagsize:])]).strip(" /")

#    def printstatus(self):
#        if not debug:
#            return
#        newstatus = self.getstatus()
#        if newstatus != self.status:
#            self.status = newstatus
#            print newstatus


class decompress:
    """bit machine for variable-sized auto-reloading tag decompression"""
    def __init__(self, data, tagsize):
        self.__curbit = 0
        self.__offset = 0
        self.__tag = None
        self.__tagsize = tagsize
        self.__in = data
        self.out = ""

    def getoffset(self):
        """return the current byte offset"""
        return self.__offset

#    def getdata(self):
#        return self.__lzdata

    def read_bit(self):
        """read next bit from the stream, reloads the tag if necessary"""
        if self.__curbit != 0:
            self.__curbit -= 1
        else:
            self.__curbit = (self.__tagsize * 8) - 1
            self.__tag = ord(self.read_byte())
            for i in xrange(self.__tagsize - 1):
                self.__tag += ord(self.read_byte()) << (8 * (i + 1))

        bit = (self.__tag  >> ((self.__tagsize * 8) - 1)) & 0x01
        self.__tag <<= 1
        return bit

    def is_end(self):
        return self.__offset == len(self.__in) and self.__curbit == 1

    def read_byte(self):
        """read next byte from the stream"""
        if type(self.__in) == str:
            result = self.__in[self.__offset]
        elif type(self.__in) == file:
            result = self.__in.read(1)
        self.__offset += 1
        return result

    def read_fixednumber(self, nbbit, init=0):
        """reads a fixed bit-length number"""
        result = init
        for i in xrange(nbbit):
            result = (result << 1)  + self.read_bit()
        return result

    def read_variablenumber(self):
        """return a variable bit-length number x, x >= 2

        reads a bit until the next bit in the pair is not set"""
        result = 1
        result = (result << 1) + self.read_bit()
        while self.read_bit():
            result = (result << 1) + self.read_bit()
        return result

    def read_setbits(self, max_, set_=1):
        """read bits as long as their set or a maximum is reached"""
        result = 0
        while result < max_ and self.read_bit() == set_:
            result += 1
        return result

    def back_copy(self, offset, length=1):
        for i in xrange(length):
            self.out += self.out[-offset]
        return

    def read_literal(self, value=None):
        if value is None:
            self.out += self.read_byte()
        else:
            self.out += value
        return False
