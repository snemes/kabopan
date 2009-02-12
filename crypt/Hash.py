import _misc
import struct
from _int import Int
class Hash:
    def __init__(self):
        self.IVs = None
        self.block_length = 8
        self.hv_size = 8
        self.output_big_endianness = False
        self.block_big_endianness = False
        self.padding_big_endianness = False

    def process_block(self, block):
        pass

    def finalize(self):
        pass

    def pad(self, message):
        return str()

    def compute(self, message):
        pass

    def digest(self):
        temp = list(self.ihvs)
        if not self.output_big_endianness:
            temp = [i.endian_swap() for i in temp]

        result = temp[0]
        for i in temp[1:]:
            result = result.concat(i)
        return result

    def hexdigest(self):
        return str(self.digest())



class merkledamgaard(Hash):

    def round_parameters(self):
        return

    def iteration_parameters(self, round):
        return

    def as_words(self, block):
        count_ = self.block_length / self.hv_size
        prefix = ">" if self.block_big_endianness else "<"
        sizes = {32:"L", 64:"Q"}
        unpack_string = prefix + str(count_) + sizes[self.hv_size]
        return [Int(i, self.hv_size) for i in list(struct.unpack(unpack_string, block))]

    def compute(self, message):
        self.ihvs = list(self.IVs)
        message += self.pad(message)
        for block in _misc.as_bytes_blocks(message, self.block_length / 8):
            self.process_block(block)
        self.finalize()
        return self
