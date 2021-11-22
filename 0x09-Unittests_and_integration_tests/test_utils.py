#!/usr/bin/env python3
"""test with the unittest"""
from utils import access_nested_map
from unittest import TestCase
from parameterized import parameterized


class TestAccessNestedMap(TestCase):
    """class that make test nestedmap"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map, path, expected):
        """test that returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


    @parameterized.expand([
        ({}, ("a",), "a"), 
        ({"a": 1}, ("a", "b"), "b")
    ])

    def test_access_nested_map_exception(self, nested_map, path):
        """test that raises exception"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))