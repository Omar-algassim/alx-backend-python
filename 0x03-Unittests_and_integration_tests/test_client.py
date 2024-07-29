#!/usr/bin/env python3
"""test client class"""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """test githuborg client"""
    @parameterized.expand([
        ('google', {'response': True}),
        ('abc', {'response': False})
    ])
    @patch('client.get_json')
    def test_org(self, input, expected, mock_get):
        """test the org methode"""
        mock_get.return_value = expected
        git = GithubOrgClient(input)
        self.assertEqual(git.org, expected)
        mock_get.assert_called_once_with(
            f"https://api.github.com/orgs/{input}"
        )

    def test_public_repos_url(self):
        """test the public repo url methode"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": 'ok'}
            git = GithubOrgClient('google')
            self.assertEqual(git._public_repos_url, 'ok')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """implement test for public_repos method"""
        mock_get_json.return_value = [{'name': 'ok'}, {'name':'good'}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repo:
            mock_public_repo.return_value = 'ok'
            git = GithubOrgClient('ok')
            self.assertEqual(git.public_repos(), ['ok', 'good'])
