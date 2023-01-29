#!/usr/bin/env python3
"""
    A module for parameterize a unit test
"""


from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
        A class for unit testing utils.access_nested_map method
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), (1)),
        ({"a": {"b": 2}}, ("a",), ({"b": 2})),
        ({"a": {"b": 2}}, ("a", "b"), (2)),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        A test for utils.access_nested_map method
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a,"), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        A test for utils.access_nested_map method for key error
        """
        self.assertRaises(KeyError)


if __name__ == "__main__":
    unittest.main()
