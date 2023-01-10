#!/usr/bin/env python3
"""
    A coroutine that measures a run time
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        excecutes async_compression fun 4 times
        using asyncio.gather
    """
    start_time = time.time()
    for i in range(4):
        await asyncio.gather(async_comprehension())
    end_time = time.time()

    return (end_time - start_time)
