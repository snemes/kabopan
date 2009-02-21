#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
Move to front

A Locally Adaptive Data Compression Scheme
J. L. Bentley, D. D. Sleator, R. E. Tarjan, V. K. Wei, 1986
"""


def move_to_front(list, offset):
    """move to the front of the list the offset-th element"""
    return [list[offset]] + list[:offset] + list[offset + 1:]


def transform(data_to_compress):
    """apply a move to front transformation

    returns the transformation vector"""
    length = len(data_to_compress)

    chars = sorted(list(set(data_to_compress)))

    result = [0 for i in range(length)]
    for i in range(length):
        index = chars.index(data_to_compress[i])
        result[i] = index
        chars = move_to_front(chars, index)

    return result


def revert(chars, vector):
    """apply a move to front reverse transformation to a list of chars
    and a transformation vector

    returns the transformed list"""
    length = len(vector)
    # assert chars == sorted(chars)

    result = ""
    for i in range(length):
        index = vector[i]
        result += chars[index]
        chars = move_to_front(chars, index)

    return result

if __name__ == "__main__":
    import kbp.test.mtf_test
