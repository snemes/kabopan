#Kabopan - Readable Algorithms. Public Domain, 2009

from entro.huffman import *
import entro._encoding as _encoding

assert pop_entry([{"symbol":"a", "weight" : 15}]) == {"symbol":"a", "weight":15}
assert pop_entry([{"node":"this"}]) == "this"


tree_test = generate_tree("a")

assert tree_test == {'symbol': 'a', 'weight': 1}
assert _encoding.generate_codes(tree_test) == {"a":""}

test_string = "abracadabra"
test_tree = generate_tree(test_string)

assert test_tree == {'left0': {'symbol': 'a', 'weight': 5},
                     'right1': {'left0': {'left0': {'symbol': 'c', 'weight': 1},
                                          'right1': {'symbol': 'd', 'weight': 1},
                                          'weight': 2},
                                'right1': {'left0': {'symbol': 'b', 'weight': 2},
                                           'right1': {'symbol': 'r', 'weight': 2},
                                           'weight': 4},
                                'weight': 6},
                     'weight': 11}

test_codes = _encoding.generate_codes(test_tree)
assert test_codes == {'a':'0', 'c':'100', 'd':'101', 'b':'110', 'r':'111'}

encoded_string = _encoding.encode(test_codes, "abracadabra")
assert encoded_string == 'n\x8a\xdc'
assert _encoding.decode(test_tree, encoded_string) == test_string
