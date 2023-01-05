#!/usr/bin/env python3
"""
    A function that takes tuples, int and returns list
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
        return the list format of the inputs(Tuple, int)
        by repating each element of lst factor times
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
