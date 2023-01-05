#!/usr/bin/env python3
"""
    Annotated function that takes
    a multiplier(float) as an argument
    and returns a function that multiplies
    a float with multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """creats a function that multiplies """
    def mul(number: float) -> float:
        """A function that multiplies floats and returns a float"""
        return number * multiplier
    return (mul)
