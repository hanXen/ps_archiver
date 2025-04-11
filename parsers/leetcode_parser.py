"""
Module: leetcode_parser

Handles fetching and parsing problem details from LeetCode.

This module includes functions to:
- Fetch problem details using LeetCode's GraphQL API.
- Parse problem metadata such as title, description, and topic tags.
- Convert problem descriptions into Markdown format.
"""


import json
from types import SimpleNamespace
from typing import Tuple

from utils.url_utils import fetch_problem_page
from utils.markdown_utils import html_to_md


def query_leetcode_problem(url: str) -> Tuple[str, str, str]:
    """
    Query LeetCode's GraphQL API to fetch problem details.

    Args:
        url (str): The URL of the LeetCode problem.

    Returns:
        Tuple[str, str, str]: Problem title, topic (if any), and description in Markdown format.
    """
    json_data = {
        "operationName": "questionData",
        "variables": {
            "titleSlug": "PLACEHOLDER"
        },
        "query": "query questionData($titleSlug: String!) {\n"
                    "  question(titleSlug: $titleSlug) {\n"
                    "    questionId\n"
                    "    title\n"
                    "    titleSlug\n"
                    "    content\n"
                    "    difficulty\n"
                    "    topicTags {\n"
                    "      name\n"
                    "      slug\n"
                    "    }\n"
                    "  }\n"
                    "}"
    }

    title_slug = url.split('/problems/')[1].split('/description')[0]
    json_data['variables']['titleSlug'] = title_slug

    problem_info = json.loads(
        fetch_problem_page("https://leetcode.com/graphql", json_data=json_data),
        object_hook=lambda x: SimpleNamespace(**x)
    ).data.question

    title = f"{problem_info.questionId}. {problem_info.title}"
    topic = f"{url.split('envId=')[1]}/" if '?' in url else ""
    description = html_to_md(problem_info.content)

    return title, topic, description
