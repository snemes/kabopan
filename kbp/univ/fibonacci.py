#Kabopan - Readable Algorithms. Public Domain, 2007-2009
"""
fibonacci encoding

Leonardo Fibonacci
universal coder
"""

from kbp.types import Str

def number(n):
    """returns the n-th fibonacci number"""
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return number(n-1) + number(n-2)


def generate_numbers(n):
    """generate all fibonacci numbers, up to the n-th"""
    result = list()
    if n == 0:
        result = [0]
    elif n >= 1:
        result = [0, 1]
        for i in xrange(2, n + 1):
            new_number = result[-1] + result[-2]
            result.append(new_number)
    return result


def decompose(value):
    """decompose a number as a sum of fibonacci numbers. returns the list of the N-th fibonacci numbers"""
    if value == 0:
        return list()
    result = list()
    numbers = [0, 1]
    n = 2
    current_number = 1
    while current_number < value:
        n += 1
        current_number = numbers[-1] + numbers[-2]
        if current_number > value:
            break
        numbers.append(current_number)
    result = [len(numbers) - 1]
    remainder = value - numbers[-1]
    result = decompose(remainder) + result
    return result


def recompose(l):
    numbers = generate_numbers(max(l))
    result = 0
    for i in l:
        result += numbers[i]
    return result


def encode(value):
    result = str()
    numbers = decompose(value)
    current = 0
    for i in range(1, max(numbers) + 1):
        result += "1" if i in numbers else "0"
    result += "1"
    #print numbers, result
    return result


def decode(string):
    encode = Str(string[:string.find("11") + 1])
    num = generate_numbers(len(encode))
    value = 0
    for i in encode.indexes("1"):
        value += num[i + 1]
    return value


if __name__ == "__main__":
    import kbp.test.fibonacci_test
