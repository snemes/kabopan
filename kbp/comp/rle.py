#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
Run-length encoding
"""

def compress(data_to_compress):
    offset = 0
    repetition = 0
    compressed_data = []
    length = len(data_to_compress)

    while offset < length:
        char = data_to_compress[offset]
        repetition = 0
        while offset + repetition < length and data_to_compress[offset + repetition] == char:
            repetition += 1

        compressed_data.append([repetition, char])
        offset += repetition
    return compressed_data


def decompress(compressed_data):
    decompressed_string = ""
    for repetition, char in compressed_data:
        decompressed_string += char * repetition
    return decompressed_string


if __name__ == "__main__":
    import kbp.test.rle_test
