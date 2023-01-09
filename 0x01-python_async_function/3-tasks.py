#!/usr/bin/env python3
"""
    A function that returns a class object; asyncio.Task
    to run the coroutines in event loops
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    """A function that returns asyncio.task"""
    return asyncio.Task(wait_random(max_delay))
