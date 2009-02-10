#Elias Delta, Gamma, Omega encoding
#universal coder
#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python



from _misc import *
import unary

def elias_split(value):
    binary = getbinstr(value)
    highest_bit = len(binary) - 1
    remaining_bits = binary[1:]
    return highest_bit, remaining_bits


def gamma_encode(value):
    highest_bit, remaining_bits = elias_split(value)
    highest_bit_encoding = unary.encode(highest_bit)
    return highest_bit_encoding + remaining_bits


def gamma_decode(binary_string):
    """reads a gamma encoded value from the binary string, return the value and the number of consumed bits"""
    assert binary_string[0] == "0"
    length, encoded_bits = unary.decode(binary_string)
    offset = length + 1
    remaining_bits = binary_string[offset: offset + length]

    read_value = (1 << length ) + getvaluefrombinarystring(remaining_bits)

    consumed_bits = length * 2 + 1
    return read_value, consumed_bits


def interleaved_gamma_encode(value):
    binary = getbinstr(value)
    remaining_bits = binary[1:]
    result = str()
    for i, c in enumerate(remaining_bits):
        result += remaining_bits[i]
        is_last_bit = (i == len(remaining_bits) - 1)
        result += "0" if not is_last_bit else "1"
    return result


def interleaved_gamma_decode(binary):
    result = 1
    offset = 0
    result = (result << 1) + int(binary[offset])
    offset += 1
    while offset < len(binary) - 2 and int(binary[offset] != 1):
        offset += 1
        result = (result << 1) + int(binary[offset])
        offset += 1
    consumed_bits = offset + 1
    return result, consumed_bits


def delta_encode(value):
    highest_bit, remaining_bits = elias_split(value)
    bits_to_encode = len(remaining_bits) + 1
    gamma = gamma_encode(bits_to_encode)
    result = gamma + remaining_bits
    return result


def delta_decode(binary_string):
    length, encoded_bits = unary.decode(binary_string)
    limit_offset = (length + 1) + length # encoding of the value itself, then 'value' number of bits to read
    first_part, next_part = binary_string[:limit_offset], binary_string[limit_offset:] # we can now extract the first encoded binary

    bits_to_decode = getvaluefrombinarystring(first_part) - 1
    value = (1 << bits_to_decode) + getvaluefrombinarystring(next_part[:bits_to_decode])

    consumed_bits = (length + 1) + length + bits_to_decode
    prin (length, limit_offset, first_part, next_part, bits_to_decode, value, consumed_bits)
    return value, consumed_bits


def omega_encode(value, first_step=True):
    if first_step == True:
        string = omega_encode(value,first_step=False) + "0"
    else:
        if value == 1:
            return str()
        else:
            encoding = getbinstr(value)
            width = len(encoding)
            string =  omega_encode(width - 1, first_step=False) + encoding
    return string


def omega_decode(binary_string, digits_to_read=1, consumed_bits=0):
    if binary_string[0] == "0":
        return digits_to_read, consumed_bits + 1
    else:
        bits = binary_string[:digits_to_read + 1]
        next_part = binary_string[digits_to_read + 1:]
        digits_to_read_next = getvaluefrombinarystring(bits)
        prin (binary_string, digits_to_read, bits, next_part, digits_to_read_next)
        return omega_decode(next_part, digits_to_read_next, consumed_bits + digits_to_read + 1)

if __name__ == "__main__":
    import elias_test