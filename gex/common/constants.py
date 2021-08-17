# -*- coding: utf-8 -*-

from gex import __version__

MARKDOWN_WELCOME = """
# Welcome
Hello there, `fellow coders` 🤖👋!

# Information
- Author:   Lucca Pessoa da Silva Matos
- GitHub:   https://github.com/lpmatos
- GitLab:   https://gitlab.com/lpmatos
"""

MARKDOWN_INTERACTIVE = """
# Interactive
"""

TIMEZONE = "America/Sao_Paulo"
DATA_FORMAT = "YYYY-MM-DD HH:mm:ss"

LOG_FORMAT = "%(levelname)s - %(asctime)s - %(message)s - %(funcName)s"
LOG_LEVELS = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"]

EX_TITLE = "GEX-tentions"
EX_DESCRIPTION = "A simple tool to make some stuffs with G-Earth"
EX_INFO = {
    "title": EX_TITLE,
    "description": EX_DESCRIPTION,
    "version": __version__,
    "author": "lpmatos",
}

EX_SETTINGS = {"use_click_trigger": True, "can_leave": True, "can_delete": True}
