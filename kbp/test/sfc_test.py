#Kabopan - Readable Algorithms. Public Domain, 2007-2009

from kbp.entro.sfc import *
import kbp.entro._encoding as encoding

assert split([0,1,2,3],1) == ([0,1], [2,3])
assert split([0,1,2,3],0) == ([0], [1,2,3])

assert split_weights([1,1]) == 0
assert split_weights([1,2,3]) == 1
assert split_weights([8,7,1]) == 0
assert split_weights([1,1,8]) == 1

assert generate_tree([{"symbol":"a", "weight":35}]) == {"symbol":"a"}
assert generate_tree([{"symbol":"a", "weight":2},
                          {"symbol":"b", "weight":2}]) == {'left0': {'symbol': 'a'},
                                                           'right1': {'symbol': 'b'}}

test_string = "abracadabra"
test_tree = encode(test_string)
assert test_tree == {'left0': {'symbol': 'a'},
                     'right1': {'left0': {'symbol': 'b'},
                                'right1': {'left0': {'symbol': 'r'},
                                           'right1': {'left0': {'symbol': 'c'},
                                                      'right1': {'symbol': 'd'}}}}}

test_codes = encoding.generate_codes(test_tree)
assert test_codes == {'a':'0', 'b':'10', 'r':'110', 'c':'1110', 'd':'1111'}
test_encoding = encoding.encode(test_codes, test_string)
assert test_encoding == 'Y\xcfX'
assert encoding.decode(test_tree, test_encoding) == test_string
