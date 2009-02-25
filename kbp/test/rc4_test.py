#Ron's Code 4, Rivest's Cipher, RC4, ARC4, ARCFOUR

from kbp.crypt.rc4 import crypt
tests = [
        ["Key", "Plaintext", '\xbb\xf3\x16\xe8\xd9@\xaf\n\xd3'],
        ["Wiki", "pedia", '\x10!\xbf\x04\x20'],
        ["Secret", "Attack at dawn", 'E\xa0\x1fd_\xc3[85RTK\x9b\xf5']
    ]

for key, message, test_value in tests:
    assert test_value == crypt(key, message)
    assert message == crypt(key, test_value)

