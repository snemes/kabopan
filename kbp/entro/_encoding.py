#Useful Functions for entropy encoding algorithms, such as Shannon Fano or Huffman
#
#Kabopan - Readable Algorithms. Public Domain, 2009


def generate_codes(node, codes=None, current_code=""):
    """walk the encoding tree and generates code for symbol (in leaves)"""
    if codes is None:
        codes = {}
    if "symbol" in node:
        codes[node["symbol"]] = current_code
        return codes
    else:
        generate_codes(node["left0"], codes, current_code + "0")
        generate_codes(node["right1"], codes, current_code + "1")
    return codes


def get_weights_and_symbols(data):
    stats = [{"symbol": chr(i), "weight": 0} for i in range(256)]
    for char in data:
        stats[ord(char)]["weight"] += 1
    stats = [i for i in stats if i["weight"] > 0]
    return stats


def encode(codes, data_to_encode):
    import kbp._bits as _bits
    comp = _bits.compress(1)
    for char in data_to_encode:
        comp.write_bitstring(codes[char])
    result = comp.getdata()
    return result

def decode(tree_root, data_to_decode):
    result = ""
    import kbp._bits as _bits
    decomp = _bits.decompress(data_to_decode, 1)
    while not decomp.is_end():
        node = tree_root
        while "symbol" not in node:
            bit = decomp.read_bit()
            if bit == 0:
                node = node["left0"]
            elif bit == 1:
                node = node["right1"]
        result += node["symbol"]
    return result
    
if __name__ == "__main__":
    import kbp.test._encoding_test