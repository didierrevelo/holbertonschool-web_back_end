#!/usr/bin/env python3
"""test client"""
from client import GithubOrgClient
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import patch


class TestGithubOrgClient(TestCase):
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """Test that GithubOrgClient.org returns the correct value."""
        client_test = GithubOrgClient(input)
        client_test.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')
