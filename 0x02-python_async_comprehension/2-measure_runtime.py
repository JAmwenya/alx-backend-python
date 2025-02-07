#!/usr/bin/env python3
"""
This module contains a coroutine to measure the runtime of four parallel
executions of async_comprehension.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of executing async_comprehension four times in parallel.

    Returns:
        float: Total runtime of the parallel execution.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
