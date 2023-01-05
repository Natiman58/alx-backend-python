#!/usr/bin/env python3
"""
    A function to annotate as required
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A function that takes a list sequence
    and returns a tuple with sequence and int
    """
    return [(i, len(i)) for i in lst]
