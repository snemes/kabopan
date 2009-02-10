from tiger import *

class tiger160(tiger):

    def digest(self):
        return tiger.digest(self)[:20]

if __name__ == "__main__":
    import test.tiger160_test
