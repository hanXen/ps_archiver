"""
Module: markdown_utils

Provides utilities for converting problem descriptions from HTML to Markdown.
"""

from markdownify import MarkdownConverter


def html_to_md(html_content: str) -> str:
    """
    Converts an HTML string into a Markdown-formatted string.

    Args:
        html_content (str): The HTML content to be converted.

    Returns:
        str: The converted Markdown string.
    """
    return MarkdownConverter().convert(html_content)


def soup_to_md(soup, **options) -> str:
    """
    Converts a BeautifulSoup object into a Markdown-formatted string.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object containing HTML content to be converted.
        **options: Additional options to customize the Markdown conversion.

    Returns:
        str: The converted Markdown string.
    """
    return MarkdownConverter(**options).convert_soup(soup)


def generate_markdown(url: str, title: str, description: str) -> str:
    """
    Generate markdown content for a problem description.

    Args:
        url (str): The URL of the problem.
        title (str): Title of the problem.
        description (str): Description of the problem.

    Returns:
        str: Generated markdown content.
    """
    return f"# {title}\n\n## 문제\n{url}\n\n{description}\n\n---\n\n## Key Points\n\n"
