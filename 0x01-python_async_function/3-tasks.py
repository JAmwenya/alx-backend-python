#!/usr/bin/env python3
"""
This module contains a function to create an asyncio task for wait_random.
"""

import asyncio
import importlib

# Import the module with an invalid name
wait_random = importlib.import_module("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
