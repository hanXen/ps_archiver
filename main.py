"""
Module: main

The entry point for the `ps_archiver` tool. 

This module handles user input, orchestrates the parsing and archiving process.
Currently supports LeetCode and Programmers platforms.
"""

import argparse
import logging

from parsers import parse_programmers_problem, query_leetcode_problem
from utils import sanitize_dir_name, save_as_markdown
from utils import generate_markdown, validate_and_transform_leetcode_url


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


supported_sites = {
    "programmers": "programmers.co.kr",
    "leetcode": "leetcode.com",
}


def main(url: str, dir_path: str = "archive") -> None:
    """
    Main function to process the given problem URL and save its description as a markdown file.

    Args:
        url (str): The URL of the problem.
        dir_path (str): Directory path to save the Markdown file.
    """
    if supported_sites.get("programmers") in url:
        url = url.split("?")[0]
        title, level, description = parse_programmers_problem(url)
        sanitized_title = sanitize_dir_name(title)
        dir_path = f"archive/{supported_sites.get("programmers")}/LV.{level}/{sanitized_title}"

    elif supported_sites.get("leetcode") in url:
        url = validate_and_transform_leetcode_url(url)
        title, topic, description = query_leetcode_problem(url)
        sanitized_topic = sanitize_dir_name(topic)
        sanitized_title = sanitize_dir_name(title)
        dir_path = f"archive/{supported_sites.get("leetcode")}/{sanitized_topic}/{sanitized_title}"

    else:
        raise NotImplementedError(f"[-] Unsupported site: {url}")

    markdown_content = generate_markdown(url, title, description)
    save_as_markdown(dir_path, markdown_content, make_solve_py=True)

    logging.info("[+] Markdown file generated successfully!")
    logging.info("[+] Path: %s/README.md", dir_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="generate problem markdown",
        description="Converts problem description to markdown.",
    )

    parser.add_argument("-u", "--url", help="The URL of the problem.", required=True)
    args = parser.parse_args()

    main(url=args.url)
