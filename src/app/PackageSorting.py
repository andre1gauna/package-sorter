
from typing import Final

MAX_BULKY_DIMENSION: Final[float] = 150.0  # cm
MAX_BULKY_VOLUME: Final[float] = 10**6     # cm³
MAX_MASS: Final[float] = 20                # kg
SPECIAL_PKG: Final[str] = "SPECIAL"
REJECTED_PKG: Final[str] = "REJECTED"       
STANDARD_PKG: Final[str] = "STANDARD"

def sort(width: int, height: int, lenght:int, mass: int ) -> str:

    _validate_inputs(width, height, lenght, mass)
    dispatch: str

    bulky = _is_bulky(width, height, lenght)
    heavy = _is_heavy(mass)

    if bulky and heavy:
        dispatch = REJECTED_PKG
    elif (bulky or heavy):
        dispatch = SPECIAL_PKG
    else:
        dispatch = STANDARD_PKG

    return dispatch   


def _is_bulky(width: int, height: int, lenght: int) -> bool:
    if (width * height * lenght >= MAX_BULKY_VOLUME) or (max(width, height, lenght) >= MAX_BULKY_DIMENSION):
        return True
    else:
        return False

def _is_heavy(mass: int) -> bool:
    return mass >= MAX_MASS
    
def _validate_inputs(width: float, height: float, length: float, mass: float) -> None:
    dims = (width, height, length, mass)
    for v in dims:
        try:
            v = float(v)
            if v is None:
                raise ValueError("Inputs must not be None.")
            if not (float("-inf") < v < float("inf")) or (v != v):
                raise ValueError("Inputs must be finite numbers.")
            if v < 0:
                raise ValueError("Inputs must be non-negative.")

        except (TypeError, ValueError):
            raise ValueError(f"Invalid input: {v}")