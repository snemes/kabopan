#unary encoding
#universal coder
#
#Kabopan - Readable Algorithms. Public Domain, 2009


"""unary is the simplest but least efficient universal coder. the encoded value is presented by a sequence of 'value' encoding bits, followed by one stopper bits.

consumed_bits is thus value + 1.
"""
def encode(value, stopper_is_1=True):
    """unary encoding. use 1 as stopper by default, 0 if specified"""
    encoder, stopper = ("0", "1") if stopper_is_1 else ("1", "0")
    return encoder * value + stopper



def decode(string, stopper_is_1=True):
    """unary decoding"""
    encoder, stopper = ("0", "1") if stopper_is_1 else ("1", "0")
    encoded_value = 0
    for i, char in enumerate(string):
        if char == encoder:
            encoded_value += 1
        elif char == stopper:
            consumed_bits = i + 1 # well, consumed_bits should be value + 1 anyway :)
            break

    return encoded_value, consumed_bits

if __name__ == "__main__":
    import test.unary_test