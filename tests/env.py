import os as _os
import sys as _sys

_PATH = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
_PATH = _os.path.join(_PATH, "src", "scripts")
_sys.path.append(_PATH)