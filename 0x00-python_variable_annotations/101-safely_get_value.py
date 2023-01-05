#!/usr/bin/env python3
"""
    Add annotations
"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')

default = Union[T, None]
rr = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: default = None) -> rr:
    """
        if there is key in dict
        return the value
    """
    if key in dct:
        return dct[key]
    else:
        return default
