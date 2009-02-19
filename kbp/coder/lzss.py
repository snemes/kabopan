#Lempel Ziv Storer Szymanski - LZSS
#lossless dictionary (sliding window) coder (compression algorithm)
#Data compression via textual substitution
#James A. Storer, Thomas G. Szymanski, 1982
#
#Kabopan - Readable Algorithms. Public Domain, 2009


import _lz77

def compress(data_to_compress):
    offset = 0
    compressed_data = []

    length = len(data_to_compress)

    while offset < length:
        match_offset, match_length = _lz77.find_longest_match(data_to_compress[:offset],
                                        data_to_compress[offset:])

        if match_length == 0:
            symbol = data_to_compress[offset]
            compressed_data.append({"literal":True, "symbol":symbol})
            offset += 1
        else:
            compressed_data.append({"literal":False, "offset":match_offset, "length":match_length})
            offset += match_length

    return compressed_data


def decompress(compressed_data):
    decompressed_data = ""

    for d in compressed_data:
        if d["literal"] == False:
            offset, length = d["offset"], d["length"]
            for i in xrange(length):
                decompressed_data += decompressed_data[-offset]
        else:
            symbol = d["symbol"]
            decompressed_data += symbol
    return decompressed_data


if __name__ == "__main__":
    import test.lszz_test
