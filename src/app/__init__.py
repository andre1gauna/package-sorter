import os
from .PackageSorting import sort
__all__ = ["sort"]

if os.getenv("ENV") == "test":
    from .PackageSorting import _is_bulky, _is_heavy, _validate_inputs
    __all__ += ["_is_bulky", "_is_heavy", "_validate_inputs"]