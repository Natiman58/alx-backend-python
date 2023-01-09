#!/usr/bin/env python3
"""
    Execute multiple coroutines at the same time in async
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
        waits for the wait_random function to complete
        return the results as a list
    """
    delays = []

    for i in range(n):
        r = await wait_random()
        if max_delay > 0:
            delays.append(r)
        else:
            delays.append(0.0)
    await asyncio.sleep(max_delay)
    return delays
