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

    def test_public_repos_url(self):
        """Test that GithubOrgClient._public_repos_url returns the correct value."""
        client_test = GithubOrgClient('google')
        with patch('client.get_json') as mock:
            mock.return_value = {'public_repos': 100}
            self.assertEqual(client_test._public_repos_url, 'https://api.github.com/orgs/google/repos')
        
