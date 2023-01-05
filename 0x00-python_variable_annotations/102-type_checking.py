#!/usr/bin/env python3
"""
    A function that takes tuples, int and returns list
"""

from typing import Tuple, List, Union, Any, SupportsIndex


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
        return the list format of the inputs(Tuple, int)
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

tup = tuple(array)

zoom_2x = zoom_array(tup)

zoom_3x = zoom_array(tup, int(3.0))
