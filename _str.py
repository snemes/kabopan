#custom string class with added methods and operators
#
#Kabopan - Readable Algorithms. Public Domain, 2009


__all__ = ["_str"]
class _str(str):
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


if __name__ == "__main__":
    import test._str_test
