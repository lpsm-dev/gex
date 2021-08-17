# -*- coding: utf-8 -*-

from rich.console import Console
from rich.markdown import Markdown

from gex import __version__
from gex.common.constants import MARKDOWN_WELCOME
from gex.common.log import Log
from gex.extension import GExtension

EX_TITLE = "GEX"
EX_DESCRIPTION = "Gex is a tool to manage G-Earth extensions write using G-Python"
EX_AUTHOR = "lpmatos"
EX_INFO = {
    "title": EX_TITLE,
    "description": EX_DESCRIPTION,
    "version": __version__,
    "author": "_Python_",
}

EX_SETTINGS = {"use_click_trigger": True, "can_leave": True, "can_delete": True}

(console, markdown, log) = (
    Console(),
    Markdown(MARKDOWN_WELCOME),
    Log("INFO", "rich", "logger").logger,
)

ext = GExtension()
