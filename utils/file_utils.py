"""
Module: file_utils

Provides utilities for saving Markdown content to files, 
including handling directory creation if necessary.
"""

import os
import re


def sanitize_dir_name(dir_name: str) -> str:
    """
    Removes characters invalid in Windows directory names.

    Args:
        dir_name (str): The directory name to sanitize.

    Returns:
        str: The sanitized directory name.
    """
    invalid_chars = r"[<>:\"/\\|?*]"
    return re.sub(invalid_chars, "", dir_name).strip()


def save_as_markdown(dir_path: str, markdown_content: str, filename: str = "README.md",
                     make_solve_py: bool = False) -> None:
    """
    Save Markdown content to a file.

    Args:
        dir_path (str): The directory path to save the file.
        markdown_content (str): The Markdown content to save.
        filename (str, optional): The name of the file. Defaults to "README.md".
        make_solve_py (bool, optional): If True, creates a `solve.py` file in the same directory.
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
    with open(f"{dir_path}/{filename}", "w", encoding="utf-8") as f:
        f.write(markdown_content)

    if make_solve_py:
        title = dir_path.split("/")[-1]
        with open(f"{dir_path}/solve.py", "w", encoding="utf-8") as f:
            f.write(f"\"\"\" solve.py for {title} \"\"\" \n\n")
