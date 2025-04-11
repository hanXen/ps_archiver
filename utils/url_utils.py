"""
Module: url_utils

This module includes functions to:
- Fetch the HTML content of a problem page.
- Validate and transform a LeetCode problem URL into the required format.
"""

import logging

import requests


def fetch_problem_page(url: str, json_data: dict = None) -> str:
    """
    Fetch the HTML content of a problem page.

    Args:
        url (str): The URL of the problem page.
        json_data (dict, optional): JSON payload for the request. Defaults to None.

    Returns:
        str: The HTML content of the fetched page.

    Raises:
        requests.exceptions.HTTPError: If the request fails.
    """
    response = requests.get(url, json=json_data, timeout=10)
    if not response.ok:
        raise requests.exceptions.HTTPError(f"[-] Failed to fetch the page: {response.status_code}")
    return response.text


def validate_and_transform_leetcode_url(url: str) -> str:
    """
    Validate and transform a LeetCode problem URL into the required format.

    Args:
        url (str): Input URL.

    Returns:
        str: Transformed URL with the required format.

    Raises:
        ValueError: If the URL is not valid.
    """
    base_url = "https://leetcode.com/problems/"

    if not url.startswith(base_url):
        raise ValueError("[-] Invalid URL: Not a LeetCode problem URL.")

    if '?' in url:
        path, query = url.split('?', 1)
    else:
        path, query = url, ""

    path_parts = path[len(base_url):].split('/')
    if len(path_parts) < 3 and (not path_parts[0] or path_parts[0] == 'description'):
        raise ValueError("[-] Invalid URL: Problem name is missing.")

    if len(path_parts) > 1 and path_parts[1] != "description":
        logging.warning("[!] URL adjusted to include 'description'.")

    problem_name = path_parts[0]
    new_path = f"{base_url}{problem_name}/description/"
    transformed_url = f"{new_path}?{query}" if query else new_path

    return transformed_url
