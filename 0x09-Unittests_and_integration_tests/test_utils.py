#!/usr/bin/env python3
"""test with the unittest"""
from utils import (access_nested_map, get_json)
from unittest import TestCase, mock
from unittest.mock import patch
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
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """test that raises exception"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(TestCase):
    """class that make test get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """test that returns what it is supposed to"""
        patchs = {'return_value.json.return_value': test_payload}
        config = patch('requests.get', **patchs)
        mock = config.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        config.stop()
