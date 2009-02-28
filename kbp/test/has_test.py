#Kabopan - Readable Algorithms. Public Domain, 2007-2009

from kbp.crypt.has import Has160
from kbp.test.common import check_test_vectors

test_vectors = \
[
    0x307964ef34151d37c8047adec7ab50f4ff89762d,
    0x4872bcbc4cd0f0a9dc7c2f7045e5b43b6c830db8,
    0x975e810488cf2a3d49838478124afce4b1c78804,
    0x2338dbc8638d31225f73086246ba529f96710bc6,
    0x596185c9ab6703d0d0dbb98702bc0f5729cd1d3c,
    0xcb5d7efbca2f02e0fb7167cabb123af5795764e5,
    0x07f05c8c0773c55ca3a5a695ce6aca4c438911b5,
]

hash_ = lambda x: Has160().compute(x).digest()
check_test_vectors(hash_, test_vectors, "HAS-160")
