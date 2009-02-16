#Lempel Ziv 77 -  LZ77 - LZ1
#lossless dictionary (sliding window) coder (compression algorithm)
#A Universal Algorithm for Sequential Data Compression
#Jacob Ziv and Abraham Lempel, 1977
#
#Kabopan - Readable Algorithms. Public Domain, 2009


import _lz77

def compress(data_to_compress):
    offset = 0
    compressed_data = []

    length = len(data_to_compress)

    while offset < length:
        #find the longest match for the next word to encode
        match_offset, match_length = _lz77.find_longest_match(data_to_compress[:offset],
                         data_to_compress[offset:])
        
        #get the next symbol, if there is something else to compress
        symbol = data_to_compress[offset + match_length] if offset + match_length < length else ''

        compressed_data.append({"offset": match_offset, "length":match_length, "symbol":symbol})
        offset += match_length + 1 # +1 since the next char is included in symbol

    return compressed_data


def decompress(compressed_data):
    decompressed_string = ""

    for d in compressed_data:
        if d["length"] != 0:
            decompressed_string = _lz77.back_copy(decompressed_string, d["length"], d["offset"])
        decompressed_string += d["symbol"]

    return decompressed_string


if __name__ == "__main__":
    import test.lz77_test
