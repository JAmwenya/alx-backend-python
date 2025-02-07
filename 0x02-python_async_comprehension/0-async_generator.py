#!/usr/bin/env python3
"""
This module contains an asynchronous generator that yields random numbers.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates 10 random numbers between 0 and 10.

    Yields:
        float: A random number.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
