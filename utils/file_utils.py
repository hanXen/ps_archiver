"""
Module: file_utils

Provides utilities for saving Markdown content to files, 
including handling directory creation if necessary.
"""


import os


def save_as_markdown(dir_path: str, markdown_content: str, filename: str = "README.md") -> None:
    """
    Save Markdown content to a file.

    Args:
        dir_path (str): The directory path to save the file.
        markdown_content (str): The Markdown content to save.
        filename (str, optional): The name of the file. Defaults to "README.md".
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
    with open(f"{dir_path}/{filename}", 'w', encoding='utf-8') as f:
        f.write(markdown_content)
