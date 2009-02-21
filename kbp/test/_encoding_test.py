#Kabopan - Readable Algorithms. Public Domain, 2007-2009

from kbp.entro._encoding import *

assert generate_codes({'left0': {'symbol': 'a', 'weight': 1},
                     'right1': {'symbol': 'b', 'weight': 1},
                     'weight': 2}) == {'a': '0', 'b': '1'}

assert get_weights_and_symbols("a") == [{"symbol":"a","weight":1}]
assert get_weights_and_symbols("abababbc") == [{"symbol":"a","weight":3},
                                               {"symbol":"b","weight":4},
                                               {"symbol":"c","weight":1},]
