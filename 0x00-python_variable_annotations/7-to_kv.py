#!/usr/bin/env python3
"""
A function to return a tuple with a string & the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns tuple where the first element is k and the second is square of v.
    """
    return (k, float(v**2))
