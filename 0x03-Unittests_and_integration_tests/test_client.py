#!/usr/bin/env python3
"""test client class"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch, MagicMock
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
            "https://api.github.com/orgs/{}".format(input)
        )
