import os

import six

class FileExistsError(OSError):
    pass

def makedirs(name, mode=0o777, exist_ok=False):
    if os.path.exists(name):
        if not exist_ok:
            raise FileExistsError("File exists: " + name)
        else:
            os.makedirs(name, mode)
import pdb;pdb.set_trace()

makedirs("pinga")
