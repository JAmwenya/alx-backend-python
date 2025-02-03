#!/usr/bin/env python3
"""
This module contains a function to measure the average runtime of a coroutine.
"""

import asyncio
import time
import importlib


wait_n  = importlib.import_module('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average runtime of wait_n(n, max_delay).
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
