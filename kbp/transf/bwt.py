#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
Burrows Wheeler Transform

A Block-sorting Lossless Data Compression Algorithm
M.Burrows, D.J. Wheeler, 1994
"""


def rotate_string(string, count):
    """rotate left a string"""
    count = count % len(string)

    result = string[count:] + string[:count]
    return result


def get_indexes(string, char):
    """returns a list of indexes of a character in a string"""
    result = []
    offset = 0

    while string[offset:].find(char) != -1:
        index = string[offset:].index(char)
        result.append(index + offset)
        offset += index + 1
    return result


def transform(data_to_compress):
    """applies Burrows-Wheeler Transform to the input data.

    returns the last column and the primary index"""
    length = len(data_to_compress)

    rotations_list = ["" for i in range(length)]

    for i in range(length):
        rotations_list[i] = rotate_string(data_to_compress, i)

    sorted_list = sorted(rotations_list)

    primary_index = sorted_list.index(data_to_compress)   # index of the original data

    last_column = ""
    for i in range(length):
        last_column += sorted_list[i][length - 1]

    return last_column, primary_index


def revert(last_column, primary_index):
    """applies a reverse Burrows Wheeler Transform.

    parameters are last column and primary index."""
    length = len(last_column)

    first_column = "".join(sorted(last_column))

    #from the first and last column, we can get the transformation vector
    transformation_vector = [0 for i in range(length)]

    chars = set(first_column)
    for char in chars:
        index_first = get_indexes(first_column, char)
        index_last = get_indexes(last_column, char)

        for i, j in enumerate(index_last):
            transformation_vector[j] = index_first[i]

    #now that we have the vector, let's generate the original string
    result = ""
    index = primary_index
    for i in range(length):
        result = last_column[index] + result
        index = transformation_vector[index]

    return result


if __name__ == "__main__":
    import kbp.test.bwt_test
