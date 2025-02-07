#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that collects random numbers
using async comprehensions.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using async comprehension.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [number async for number in async_generator()]
