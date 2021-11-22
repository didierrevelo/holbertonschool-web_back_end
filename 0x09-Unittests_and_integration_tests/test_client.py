#!/usr/bin/env python3
"""test client"""
from client import GithubOrgClient
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import patch, PropertyMock


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
        """Test that GithubOrgClient._public_repos_url
        returns the correct value."""
        client_test = GithubOrgClient('google')
        with patch('client.get_json') as mock:
            mock.return_value = {'public_repos': 100}
            self.assertEqual(client_test._public_repos_url,
                             'https://api.github.com/orgs/google/repos')

    @patch('client.get_json')
    def test_public_repos(self, mock_j):
        """Test that GithubOrgClient.public_repos returns the correct value."""
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_j.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_j.assert_called_once()
