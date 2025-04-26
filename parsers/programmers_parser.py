"""
Module: programmers_parser

Handles fetching and parsing problem details from the Programmers platform.

This module includes functions to:
- Fetch the problem description's HTML content from programmers.co.kr.
- Extract problem metadata (title, level, description) from HTML.
- Convert problem descriptions into Markdown format.
"""

import logging
from typing import Tuple

from bs4 import BeautifulSoup

from utils import fetch_problem_page, soup_to_md


def parse_programmers_problem(url: str) -> Tuple[str, str, str]:
    """
    Parse problem details from a Programmers problem page.

    Args:
        url (str): The URL of the Programmers problem page.

    Returns:
        Tuple[str, str, str]: Problem title, level, and description in Markdown format.

    Raises:
        NotImplementedError: If the page structure has changed and cannot be parsed.
    """
    html = fetch_problem_page(url)
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("span", class_="challenge-title").text.strip()
    level = soup.find("div", class_="lesson-content")["data-challenge-level"]
    description = soup.find("div", class_="guide-section-description")

    if not (title and level and description):
        logging.debug("Title: %s | Level: %s | Description:\n%s", title, level, description)
        raise NotImplementedError("[-] programmers.co.kr may be updated.")

    for header_tag in soup.find_all(["h5", "h6"]):
        header_tag.name = "h3"

    description = soup_to_md(description).strip()

    return title, level, description
