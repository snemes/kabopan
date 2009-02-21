#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
Range encoding

entropy encoding
Range encoding: an algorithm for removing redundancy from a digitized message
G.N.N Martin, 1979
"""

import pprint
from fractions import Fraction

def common_string(a,b):
    """return a string made of all the common digits and the half of the first different digits"""
    assert a != b
    string_a = `a`
    string_b = `b`

    i = 0
    while string_a[i] == string_b[i]:
        i += 1
    common_digits = string_a[:i]
    last_digit = chr( (ord(string_a[i]) + ord(string_b[i])) / 2)
    return common_digits + last_digit

#assert common_string(74320295 , 74320338) == 7432

#TODO : put in _misc
def get_symbols_and_frequencies(data):
    elements = [{"symbol": chr(i), "weight": 0} for i in range(256)]    # this will store symbols, and their weights

    for char in data:
        elements[ord(char)]["weight"] += 1

    elements = [e for e in elements if e["weight"] > 0]
    return elements

def do(data_to_compress):
    elements = get_symbols_and_frequencies(data_to_compress)

    symbols = [e["symbol"] for e in elements]

    total_weight = sum(e["weight"] for e in elements)

    # now we have all present symbols, and their frequency as weight
    # we'll calculate the probabilistic range for each symbol
    last_low = 0
    for e in elements:
        probability = Fraction(e["weight"],total_weight)
        low, high = last_low, last_low + probability
        e["range"] = [low, high]

        last_low = high

    scale = 1 #0 ** len(data_to_compress)
    current_low, current_high = (Fraction(0), Fraction(scale))
    for char in data_to_compress:
        current_width = current_high - current_low

        # now we want the probabilistic range of the current symbol
        char_index = symbols.index(char)
        element = elements[char_index]
        symbol_range_low, symbol_range_high = element["range"]

        # we can now calculate the sub range for the current symbol
        current_low, current_high = (current_low + symbol_range_low * current_width,
                                     current_low + symbol_range_high * current_width)

    return current_low, current_high


"""
L = 0.0
H = 1.0
Start_Loop
R = H - L
H = L + R * H_of_i_th_symbol
L = L + R * L_of_i_th_symbol
Loop_Until_the_Last_Symbol_is_Processed
Output something_between_L_and_H

X = encoded_number
Start Loop
Find_range_enclosing_X
Output the_symbol_of_the_range_found
R = H_of_symbol_found - L_of_symbol_found
X = (X - L_of_symbol_found) / R
Loop_until_the_last_symbol_output
"""

if __name__ == "__main__":
    import kbp.test.range_test
