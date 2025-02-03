#!/usr/bin/env python3
"""
This module contains a function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier.
    """
    return lambda x: x * multiplier
