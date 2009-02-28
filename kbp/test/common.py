#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""common functions for test files"""

test_vector_strings = [
    "",
    "a",
    "abc",
    "message digest",
    "abcdefghijklmnopqrstuvwxyz",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
    "1234567890" * 8]

def check_test_vectors(hash_, test_vectors, function=""):
    for i, s in enumerate(test_vector_strings):
        expected = test_vectors[i]
        result = hash_(s)
        if result != expected:
            template = """
            {function} test vectors:
                expected
                {expected}
                result
                {result}"""
            errormsg = template.format(function=function, expected=expected, result=result)
            raise AssertionError(errormsg)