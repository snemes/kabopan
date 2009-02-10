from tiger import *

class tiger128(tiger):

    def digest(self):
        return tiger.digest(self)[:16]

if __name__ == "__main__":
    import test.tiger128_test
