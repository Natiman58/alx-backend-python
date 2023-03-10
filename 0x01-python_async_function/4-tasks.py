#!/usr/bin/env python3
"""
    return a result as a list
"""
import asyncio
from typing import List

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        waits for the wait_random function to complete
        return the results as a list
    """
    coroutines = []

    for i in range(n):
        coroutines.append(task_wait_random(max_delay))
    L = sorted(await asyncio.gather(*coroutines))
    return L
