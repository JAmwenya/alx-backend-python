#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine to wait for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for random delay between 0 - max_delay seconds & returns the delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
