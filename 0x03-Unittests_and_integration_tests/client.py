#!/usr/bin/env python3
"""
Client for interacting with GitHub API
"""

from typing import Any, List, Dict
from utils import get_json, memoize


class GithubOrgClient:
    """
    A client for GitHub organization information
    """

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str):
        """
        Initialize the client with the organization name
        Args:
            org_name (str): The name of the organization
        """
        self.org_name = org_name

    @memoize
    def org(self) -> Dict:
        """
        Get the organization information
        Returns:
            Dict: The organization information
        """
        url = self.ORG_URL.format(org=self.org_name)
        return get_json(url)

    @property
    def _public_repos_url(self) -> str:
        """
        Get the URL for the public repositories
        Returns:
            str: The URL for the public repositories
        """
        return self.org.get("repos_url", "")

    def public_repos(self, license_key: str = None) -> List[str]:
        """
        Get the list of public repositories
        Args:
            license_key (str): The license key to filter repositories by
        Returns:
            List[str]: The list of repository names
        """
        url = self._public_repos_url
        repos = get_json(url)
        repo_names = [repo["name"] for repo in repos]

        if license_key:
            repo_names = [
                repo["name"]
                for repo in repos
                if repo.get("license", {}).get("key") == license_key
            ]

        return repo_names

    def has_license(self, repo: Dict[str, Any], license_key: str) -> bool:
        """
        Check if a repository has a specific license
        Args:
            repo (Dict[str, Any]): The repository information
            license_key (str): The license key to check for
        Returns:
            bool: True if the repository has the license, False otherwise
        """
        license_info = repo.get("license")
        return license_info is not None and license_info.get("key") == license_key
