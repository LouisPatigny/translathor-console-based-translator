# utils.py
"""
Utility functions for the application.
"""


def display_banner():
    """
    Displays the application banner.
    """
    banner = """
    ============================================
          Welcome to the Translation Tool
    ============================================
    """
    print(banner)


def get_user_input(prompt):
    """
    Safely gets input from the user.

    Args:
        prompt (str): The input prompt to display.

    Returns:
        str: The user's input.
    """
    try:
        return input(prompt).strip()
    except EOFError:
        return ''
