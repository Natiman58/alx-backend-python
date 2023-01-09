#!/usr/bin/env python3
"""
    Execute multiple coroutines at the same time in async
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        waits for the wait_random function to complete
        return the results as a list
    """
    coroutines = []

    for i in range(n):
        coroutines.append(wait_random(max_delay))
    L = sorted(await asyncio.gather(*coroutines))
    return L
