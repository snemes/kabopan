#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
Lempel Ziv Welch - LZW

lossless dictionary (dynamic) coder (compression algorithm)
A Technique for High-Performance Data Compression
Terry A. Welch, 1984
"""


def compress(data_to_compress):
    """compress using LZW.
    return roots (present symbols in the data to compress)
    and the LZW-compressed data (indexes representing either an entry in the dictionary, or the need to create a new entry)"""
    offset = 0
    compressed_data = []
    roots = list(set(data_to_compress))
    dictionary = list(roots)   # at the start, the dictionary contains all possible symbols

    word = ''
    for char in data_to_compress:
        if (word + char) in dictionary: # expand word with the next char
            word = word + char          # as long as it's present in the dictionary
        else:
            # write down the last corresponding entry in the dictionary
            compressed_data.append(dictionary.index(word))
            #create new entry with extra char
            dictionary.append(word + char)
            #resume loop with that char
            word = char
        offset += 1
    compressed_data.append(dictionary.index(word)) # don't forget the remaining word

    return roots, compressed_data


def decompress(roots, compressed_data):
    dictionary = list(roots)

    #the first index has to be one of the root. decompressed_data is started.
    first_index = compressed_data[0]
    first_char = dictionary[first_index]
    decompressed_data = first_char
    
    current_index = first_index

    #now we'll read all the remaining indexes, and remember the previous one
    for index in compressed_data[1:]:
        previous_index = current_index
        current_index = index

        previous_word = dictionary[previous_index]
        previous_initial = previous_word[0]

        if current_index < len(dictionary):                # existing entry ?

            current_word = dictionary[current_index]
            current_initial = dictionary[current_index][0]

            new_word = previous_word + current_initial
            decompressed_data += current_word
            
            dictionary.append(new_word)
        else:
            # current_index == len(dictionary) except for last iteration
            new_word = previous_word + previous_initial
            decompressed_data += new_word

            dictionary.append(new_word)

    return decompressed_data


if __name__ == "__main__":
    import kbp.test.lzw_test
