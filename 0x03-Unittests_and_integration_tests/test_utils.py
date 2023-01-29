#!/usr/bin/env python3
"""
    A module for parameterize a unit test
"""


from unittest import mock
from unittest.mock import patch
import utils
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
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a,"), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        A test for utils.access_nested_map method for key error
        """
        self.assertRaises(KeyError)


class TestGetJson(unittest.TestCase):
    """
        A class for unit testing utils.get_json method
    """
    @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_response):
        """
        A test for utils.get_json method
        Make sure it returns a Mock object
        with a json method that returns test_payload
        and check if the mock obj is called exactly once with test_url
        """
        mock_response.return_value.json.return_value = test_payload
        self.assertEqual(utils.get_json(test_url), test_payload)
        mock_response.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
        A class for unit testing utils.memoize method
    """
    def test_memoize(self):
        """
        A test for utils.memoize method
        when calling the a_property make sure a_method is called
        memoize a_propery so that
        if a_propery is called twice a_method is called once

        """
        class TestClass:
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            thing = TestClass()
            thing.a_property()
            thing.a_property()
        mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
