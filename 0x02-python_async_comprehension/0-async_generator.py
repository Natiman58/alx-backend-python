#!/usr/bin/env python3
"""
    An async generator function
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
        Loops 10 times and each time the loop waits for one sec
        then yields a random number between 0 - 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)