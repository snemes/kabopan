#US Secure Hash Algorithm 1 (SHA1)
#RFC 3174
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from sha0 import sha0

class sha1(sha0):

    def compress(self, block, words):
        words.extend(0 for i in xrange(80 - 16))
        for i in range(16, 80):
            words[i] = words[i - 3] ^ words[i - 8] ^ words[i - 14] ^ words[i - 16]
            # a rotation was added between sha0 and sha1
            words[i] = words[i].rol(1)
        return words

if __name__ == "__main__":
    import test.sha1_test
