#!/usr/bin/env python3
"""utils test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, MagicMock


class TestAccessNestedMap(unittest.TestCase):
    """test the utils function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """test error raise"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """test http request"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, expected):
        """test get json function not really request"""
        with patch('utils.requests') as mock_get:
            mock_response = MagicMock()
            mock_response.json.return_value = expected
            mock_get.get.return_value = mock_response
            self.assertEqual(get_json(url), expected)


class TestMemoize(unittest.TestCase):
    """test the memoize"""

    def test_memoize(self):
        """test the memoize function"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass,
                          'a_method',
                          return_value=lambda: 42) as mock:
            test = TestClass()
            self.assertEqual(test.a_property(), 42)
            self.assertEqual(test.a_property(), 42)
            mock.assert_called_once()
