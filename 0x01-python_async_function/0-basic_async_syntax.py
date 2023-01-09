#!/usr/bin/env python3
"""
    Async method
"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
        An asynchronous coroutine
        that waits for a random delay b/n 0 - max_delay
        including float value seconds and
        return the total delay
    """
    total_delay = random.random() * max_delay
    await asyncio.sleep(total_delay)
    return total_delay
