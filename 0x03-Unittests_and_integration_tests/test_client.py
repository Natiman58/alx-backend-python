#!usr/bin/env python3
"""
This is a simple script to run the main.py file.
"""

from typing import Dict
import unittest
from unittest.mock import MagicMock, patch
from parameterized import parameterized
import client


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


__name__ = "__main__":
    unittest.main()
