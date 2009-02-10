#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from code.base import *

assert base8 == "01234567"
assert base16 =="0123456789ABCDEF"
assert base32 == "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
assert base32_hex == "0123456789ABCDEFGHIJKLMNOPQRSTUV"
assert base64 == "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
assert base64_safe == "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"


test_string = "Man is distinguished, not only by his reason, " \
"but by this singular passion from other animals, which is a lust of the mind," \
" that by a perseverance of delight in the continued and indefatigable generation of knowledge," \
" exceeds the short vehemence of any carnal pleasure."

encoded_string = "TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbm" \
"d1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQs"\
"IHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZm"\
"F0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ug"\
"b2YgYW55IGNhcm5hbCBwbGVhc3VyZS4="
assert encode_base64(test_string) == encoded_string
assert decode_base64(encode_base64(test_string)) == test_string
assert decode_base64(encode_base64(test_string[:-1])) == test_string[:-1]
assert decode_base64(encode_base64(test_string[:-2])) == test_string[:-2]

assert encode_base64("") == ""
assert encode_base64("f") == "Zg=="
assert encode_base64("fo") == "Zm8="
assert encode_base64("foo") == "Zm9v"
assert encode_base64("foob") == "Zm9vYg=="
assert encode_base64("fooba") == "Zm9vYmE="
assert encode_base64("foobar") == "Zm9vYmFy"

assert encode_base32("") == ""
assert encode_base32("f") == "MY======"
assert encode_base32("fo") == "MZXQ===="
assert encode_base32("foo") == "MZXW6==="
assert encode_base32("foob") == "MZXW6YQ="
assert encode_base32("fooba") == "MZXW6YTB"
assert encode_base32("foobar") == "MZXW6YTBOI======"

assert encode_base32hex("") == ""
assert encode_base32hex("f") == "CO======"
assert encode_base32hex("fo") == "CPNG===="
assert encode_base32hex("foo") == "CPNMU==="
assert encode_base32hex("foob") == "CPNMUOG="
assert encode_base32hex("fooba") == "CPNMUOJ1"
assert encode_base32hex("foobar") == "CPNMUOJ1E8======"

assert encode_base16("") == ""
assert encode_base16("f") == "66"
assert encode_base16("fo") == "666F"
assert encode_base16("foo") == "666F6F"
assert encode_base16("foob") == "666F6F62"
assert encode_base16("fooba") == "666F6F6261"
assert encode_base16("foobar") == "666F6F626172"

#just for fun, it doesn't work perfectly because padding char lose their width
#print encode_base64("coincoin"), decode(encode("coincoin", base256, base32), base64, base32)