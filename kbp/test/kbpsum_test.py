import os
with os.tmpfile() as f: #empty
    pass
with os.tmpfile() as f: #million a
    f.write("a"* 10 ** 6)
