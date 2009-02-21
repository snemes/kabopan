#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
Flechter checksum - Flechter-16/32

An Arithmetic Checksum for Serial Transmissions.
Fletcher, J. G.
1982
"""

def compute(data_to_checksum, size, modulo, limit=None):
    sum, sum_of_sum = 1, 0

    length = len(data_to_checksum)
    if limit is not None and length > limit:
        data_to_checksum = data_to_checksum[:limit]
    for char in data_to_checksum:
        sum += ord(char)
        sum_of_sum += sum
        sum %= modulo
        sum_of_sum %= modulo
    return (sum_of_sum << (size / 2)) + sum


def fletcher16(data_to_checksum):
    return compute(data_to_checksum, 8, limit=21)


def fletcher32(data_to_checksum):
    return compute(data_to_checksum, 32, 65535, limit=360)

if __name__ == "__main__":
    import kbp.test.fletcher_test
