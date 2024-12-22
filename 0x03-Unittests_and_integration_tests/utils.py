#!/usr/bin/env python3
"""
Utility functions and classes
"""

from typing import Mapping, Any, Sequence
import requests


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """
    Access a nested map with a sequence of keys.
    Args:
        nested_map (Mapping): The nested map to access.
        path (Sequence): A sequence of keys leading to the desired value.
    Returns:
        Any: The value at the end of the path.
    Raises:
        KeyError: If the path is invalid.
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map


def get_json(url: str) -> Any:
    """
    Make a GET request to a URL and return the JSON response.
    Args:
        url (str): The URL to make the GET request to.
    Returns:
        Any: The JSON response from the URL.
    """
    response = requests.get(url)
    return response.json()


def memoize(method):
    """
    Memoize a method to cache its return value after the first call.
    Args:
        method (Callable): The method to memoize.
    Returns:
        Callable: The memoized method.
    """
    attr_name = f"_memoized_{method.__name__}"

    def memoized(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, method(self))
        return getattr(self, attr_name)

    return memoized
