#!/usr/bin/env python3
"""
    This is a simple script to run the main.py file.
"""

from typing import Dict
import unittest
from unittest import mock
from unittest.mock import MagicMock, PropertyMock, patch
from parameterized import parameterized
import client
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
        This is a test class for the GithubOrgClient class.
    """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch('client.get_json')  # patch where the method is called
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """Tests the `org` method."""
        mocked_fxn.return_value = MagicMock(return_value=resp)
        gh_org_client = client.GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)

        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self,):
        """ A mock test for _public_repos_url method
            using patch as a context manager
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = {
                'repos_url': 'https://api.github.com/users/google/repos',
            }
            self.assertEqual(GithubOrgClient("github")._public_repos_url,
                             'https://api.github.com/users/google/repos')

    @patch('client.get_json', return_value=[{'name': 'license1'},
                                            {'name': 'license2'},
                                            {'name': 'license3'}])
    def test_public_repos(self, mock_client):
        """
            using patch as a decorator and context manager
            to mock test get_json and _public_repos methods
            respectively

        """
        url = "https://api.github.com"
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value=url) as mock_public_repos:
            test_clinet = GithubOrgClient('client').public_repos()
            for i in range(3):
                self.assertIn(mock_client.return_value[i]['name'], test_clinet)

            mock_client.assert_called_once()
            mock_public_repos.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test the has_license method
        """
        test_licence = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(test_licence, expected)
