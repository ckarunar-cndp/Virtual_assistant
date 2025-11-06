"""
Tabs package initializer.

This package contains all tab-related modules used in VA_v1.py:
- tab_email: Handles email tab UI and logic
- tab_summary: Displays summaries
- tab_edit: Handles text editing
- tab_ocr: Optical character recognition tab
- tab_about: About/info tab
"""

from .tab_email import show_email_tab
from .tab_summary import show_summary_tab
from .tab_edit import show_edit_tab
from .tab_ocr import show_ocr_tab
from .tab_about import show_about_tab

__all__ = [
    "show_email_tab",
    "show_summary_tab",
    "show_edit_tab",
    "show_ocr_tab",
    "show_about_tab",
]
