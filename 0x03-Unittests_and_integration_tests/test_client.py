#!/usr/bin/env python3
"""
Unit and Integration tests for client.py
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class to test GithubOrgClient methods
    """

    @parameterized.expand(
        [
            ("google",),
            ("abc",),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value
        """
        mock_get_json.return_value = {"login": org_name}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {"login": org_name})
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test _public_repos_url property
        """
        mock_org.return_value = {"repos_url": "https://api.github.com/repos"}
        client = GithubOrgClient("test_org")
        self.assertEqual(client._public_repos_url, "https://api.github.com/repos")

    @patch("client.get_json")
    @patch("client.GithubOrgClient._public_repos_url", new_callable=PropertyMock)
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """
        Test public_repos method
        """
        mock_repos_url.return_value = "https://api.github.com/repos"
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]

        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), ["repo1", "repo2"])
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/repos")

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected):
        """
        Test has_license method
        """
        client = GithubOrgClient("test_org")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class(
    [
        {
            "org_payload": {"repos_url": "https://api.github.com/repos"},
            "repos_payload": [{"name": "repo1"}, {"name": "repo2"}],
            "expected_repos": ["repo1", "repo2"],
        },
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for GithubOrgClient
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class with patcher for requests.get
        """
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload,
            cls.repos_payload,
        ]

    @classmethod
    def tearDownClass(cls):
        """
        Stop patcher
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos integration
        """
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), self.expected_repos)
