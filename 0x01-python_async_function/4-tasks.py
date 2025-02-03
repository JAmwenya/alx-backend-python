#!/usr/bin/env python3
"""
This module contains a function to execute multiple tasks concurrently.
"""

import asyncio
import importlib
from typing import List
task_wait_random = importlib.import_module("0-basic_async_syntax").wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes task_wait_random n times and returns the list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
