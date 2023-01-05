#!/usr/bin/env python3
"""
    A function that takes mxd_list of integers and floats
    as argument and return their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Takes list of floats and integers
        then returns their sum as float
    """
    return sum(mxd_lst)
