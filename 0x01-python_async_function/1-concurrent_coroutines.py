#!/usr/bin/env python3
"""
This module contains a coroutine to execute multiple coroutines concurrently.
"""

import asyncio
import importlib
from typing import List

# Import the module with an invalid name
wait_random = importlib.import_module("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times and returns the list of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
