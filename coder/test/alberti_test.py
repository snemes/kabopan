#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from coder.alberti import *


assert switch_alphabet("ab", "cd", "b") == "d"


assert encrypt_mode1("LAGVER2RASIFARA", "g") == "zgthpmamgqurgmg"


assert decrypt_mode1("AzgthpmamgQlfiyky", "g") == "LAGVERRASIFARA"
assert decrypt_mode1("zgthpmamgqurgmg", "g") == "LAGVERRASIFARA"


assert encrypt_mode2("LAGVERASIFARA", "m") ==  "cmbufpmradmpm"
assert encrypt_mode2("LAGVERA3SIFARA", "m") == "cmbufpmsndhsls"


assert decrypt_mode2("cmbufpmsndhsls", "m") == "LAGVERASIFARA"
