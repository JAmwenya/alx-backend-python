#!/usr/bin/env python3
"""
Unit tests for utils.py
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class to test utils.access_nested_map
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map returns expected result
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",)),
            ({"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access_nested_map raises KeyError for invalid path
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class to test utils.get_json
    """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test utils.get_json returns the expected result
        """
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    TestMemoize class to test utils.memoize decorator
    """

    def test_memoize(self):
        """
        Test that a_method is only called once when memoized
        """

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            obj = TestClass()
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            mock_method.assert_called_once()
