#!/usr/bin/env python3
"""
    Annotated function that takes a string k and v (an int or float)
    as argument and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes k(string) and v(int or float)
        and returns a tuple of str and float"""
    return (k, v**2)
