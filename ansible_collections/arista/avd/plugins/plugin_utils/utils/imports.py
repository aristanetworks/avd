from __future__ import annotations
from typing import TextIO
import sys
import warnings


def custom_showwarning(
    message: str | Warning, category: type[Warning], filename: str, lineno: int, file: TextIO | None = None, line: str | None = None
) -> None:
    """
    As suggested in Python3 documentation, patching showwarning to display our own warnings
    """
    WARNING = "\033[93m"
    END = "\033[0m"
    BOLD = "\033[1m"
    print(f"{WARNING}{BOLD}{category.__name__}: {filename}:{lineno} {message}{END}", file=sys.stderr)


class AVDWarning(UserWarning):
    pass


def warning_on_fail_import(message: str, filename: str, lineno: int):
    warnings.showwarning = custom_showwarning
    warnings.showwarning(message, AVDWarning, filename, lineno)
