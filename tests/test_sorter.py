import pytest
import math

from app.PackageSorting import sort

@pytest.mark.parametrize(
"w, h, l, m, expected",
     [
        (10, 10, 10, 1, "STANDARD"),
        (149.9, 149.9, 0.1, 2, "STANDARD"),
        (50, 50, 50, 10, "STANDARD"),          
        (149, 149, 1, 19.9, "STANDARD"),       
        (149.5, 10, 10, 5, "STANDARD"),       
        (10, 10, 149.99, 1, "STANDARD"),  

        (149.9999, 149.9999, 149.9999, 19.9999, "SPECIAL"),
        (1, 150, 1, 1, "SPECIAL"),
        (1, 1, 150, 1, "SPECIAL"),
        (150.0, 10.0, 10.0, 19.0, "SPECIAL"),
        (50.5, 50.5, 78.5, 20.0, "SPECIAL"),
        (1, 1, 1, 20, "SPECIAL"),

        (150, 150, 1, 20, "REJECTED"),         
        (100, 100, 100, 25, "REJECTED"),
        (200, 50, 20, 25, "REJECTED"),         
        (100, 100, 100, 20, "REJECTED"),       
        (300, 300, 1, 50, "REJECTED"),         
        (151, 149, 149, 20, "REJECTED")
    ]
)
def test_sort_valid_inputs(w, h, l, m, expected):
    assert sort(w, h, l, m) == expected

@pytest.mark.parametrize("bad", [None, -10, -0.1, float("-inf"), float("inf"), math.nan])
def test_sort_invalid_inputs(bad):
    valid = (10,10,10,10)

    for i in range(4):
        args = list(valid)
        args[i] = bad
        with pytest.raises(ValueError):
            sort(*args)

    
