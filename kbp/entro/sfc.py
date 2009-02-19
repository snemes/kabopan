#Shannon-Fano coding
#Entropy encoding
#A Mathematical Theory of Communication
#Claude E. Shannon, 1948
#
#Kabopan - Readable Algorithms. Public Domain, 2009


import _encoding

def split(list, index):
    """split the list in 2 halves AFTER the index parameter"""
    return list[:index + 1], list[index + 1:]


def split_weights(weights):
    """returns the index of a list of weight, after which the list is split in 'almost equal' halves
    ie when the difference of cumulated weights of both parts is minimal"""
    length = len(weights)

    increasing_weights = [sum(weights[:i + 1]) for i in range(length)]
    decreasing_weights = [sum(weights[i:]) for i in range(length)]
    differences = [abs(increasing_weights[i] - decreasing_weights[i + 1])
                   for i in range(length - 1)]

    half_weight = min(differences)
    half_index = differences.index(min(differences))
    return half_index


def generate_tree(elements):
    """generate a shannon fano tree out of a list of dictionaries of symbols and their weights"""
    if len(elements) == 1:
        node = {"symbol":elements[0]["symbol"]} # nothing to split - it's a leaf
    else:
        weights = [e["weight"] for e in elements]
        half_weight_index = split_weights(weights)

        left_half, right_half = split(elements, half_weight_index)

        left_node = generate_tree(left_half)
        right_node = generate_tree(right_half)

        node = {"left0": left_node, "right1": right_node}

    return node


def encode(data_to_compress):
    stats = _encoding.get_weights_and_symbols(data_to_compress)

    stats = sorted(stats, key = lambda x:x["weight"], reverse = True)

    tree = generate_tree(stats)

    return tree


if __name__ == "__main__":
    import kbp.test.sfc_test
