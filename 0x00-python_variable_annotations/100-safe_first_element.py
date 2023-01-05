#!/usr/bin/env python3
"""
    Give the correct duck type annotations
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        if there is list return the first element
        else: return none
    """
    if lst:
        return lst[0]
    else:
        return None
