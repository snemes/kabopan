from distutils.core import setup
import py2exe
setup(console=['kbpsum.py', 'kbpentro.py', 'kbpuniv.py'], 
    options=
        {"py2exe":
            { "optimize":1, "ascii":True, "bundle_files":2,"compressed":1,
            }, 
        }
    )