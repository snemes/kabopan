#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
Base2, Base8, Base16, Base32, Base32hex, Base64

coder
The Base16, Base32, and Base64 Data Encodings, rfc 3548
S. Josefsson, 2003
"""

from kbp._misc import (
 DIGITS, ALPHABET, ALPHABET_LOWERCASE, ASCII, char_range,
 getbinlen, getpadbinstr, getvaluefrombinarystring,
 lcm)


base2 = "01"
base8 = char_range("0", "7")
base16 = DIGITS + char_range("A", "F")
base32 = ALPHABET + char_range("2", "7")
base32_hex = DIGITS + char_range("A", "V")
base64 = ALPHABET + ALPHABET_LOWERCASE + DIGITS + "+/"
base64_safe = ALPHABET + ALPHABET_LOWERCASE + DIGITS + "-_"
base256 = ASCII


def quotient_ceiling(dividend, divisor):
    quotient, remainder = divmod(dividend, divisor)
    if remainder > 0:
        quotient += 1
    return quotient


def change_base(block, block_length, source_base, source_size, target_base, target_size):
    """takes block as a block_length-bit long binary stream.
    reads it as entries of source_base, on source_size bits,
    resplit bits as target_base chars, which are stored on target_size"""

    #let's get a binary representation of our block, in our source base
    bits_string = ""
    for char in list(block):
        bits_string += getpadbinstr(source_base.index(char), source_size)

    #then split that representation in target_size bits long blocks
    split_bits = (bits_string[i: i + target_size] for i in range(0,  block_length, target_size))

    #get the according values,
    encoded_values = (getvaluefrombinarystring(i) for i in split_bits)
    #and the corresponding entries from our target base
    output_chars = [target_base[i] for i in encoded_values]
    output_block = "".join(output_chars)

    return output_block

def get_params(source_base, target_base):
    """takes 2 bases, calculate the bit-length they have to be encoded in,
    the common block length both can be encoded in,
    and the amount of symbols contained in that block, for each base"""
    source_width, target_width = [getbinlen(len(b) - 1) for b in [source_base, target_base]]    # how many bits necessary to encode a base
    block_width = lcm(source_width, target_width) # smallest block bit-length to store both

    source_length, target_length = [block_width / i for i in [source_width, target_width]] # how many chars to read to fill a block
    return block_width, source_width, source_length, target_width, target_length


def encode(data_to_encode, source_base, target_base, padding_char="="):

    block_width, source_width, source_length, target_width, target_length = get_params(source_base, target_base)
    length = len(data_to_encode)
    encoded_data = ""

    #let's process the data to encode via source_length-chars long blocks
    blocks = (data_to_encode[i:i + source_length] for i in range(0, length, source_length))

    for block in blocks:
        padding = 0

        #any padding required for current block ?
        block_length = len(block)
        if block_length < source_length:
            #let's get how many chars we need to encode that block
            input_bits = block_length * source_width
            needed_chars = quotient_ceiling(input_bits, target_width)
            padding = target_length - needed_chars

            # and now we get how many chars we have do add for padding
            missing_chars = source_length - block_length
            block += source_base[0] * missing_chars

        output_block = change_base(block, block_width, source_base, source_width , target_base, target_width)

        #if that block has to be padded, we'll replace the correct amount of trailing chars
        if padding:
            output_block = output_block  [:needed_chars] + padding_char * padding

        #and output our result
        encoded_data += output_block
    return encoded_data


def decode(data_to_decode, source_base, target_base, padding_char="="):

    block_width, source_width, source_length, target_width, target_length = get_params(source_base, target_base)

    length = len(data_to_decode)
    decoded_data = ""

    #let's process the data to decode via target_length-chars long blocks
    blocks = (data_to_decode[i: i + target_length] for i in range(0, length, target_length))

    for block in blocks:

        #is that block padded ?
        padding = block.count(padding_char)
        if padding:
            #let's calculate how many chars were encoded in the first place
            used_chars = target_length - padding
            used_bits = used_chars * target_width
            encoded_chars = used_bits / source_width
            #replace padded chars with the 0 bit char of our target encoding
            block = block.replace(padding_char, target_base[0])

        output_block = change_base(block, block_width, target_base, target_width, source_base, source_width)

        #if that block was padded, then we'll truncate the extra bytes
        if padding:
            output_block = output_block[:encoded_chars]

        decoded_data += output_block
    return decoded_data


def encode_base64(data):
    result = encode(data, base256, base64)
    assert data == decode(result, base256, base64)  # just for testing
    return result

def decode_base64(data):
    return decode(data, base256, base64)

def encode_base32(data):
    result = encode(data, base256, base32)
    assert data == decode(result, base256, base32)  # just for testing
    return result

def decode_base32(data):
    return decode(data, base256, base32)

def encode_base32hex(data):
    result = encode(data, base256, base32_hex)
    assert data == decode(result, base256, base32_hex)  # just for testing
    return result

def decode_base32hex(data):
    return decode(data, base256, base32_hex)

def encode_base16(data):
    result = encode(data, base256, base16)
    assert data == decode(result, base256, base16)  # just for testing
    return result

def decode_base16(data):
    return decode(data, base256, base16)


if __name__ == "__main__":
    import kbp.test.base_test