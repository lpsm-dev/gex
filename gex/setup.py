# -*- coding: utf-8 -*-

from rich.console import Console
from rich.markdown import Markdown

from gex import __version__
from gex.common.constants import MARKDOWN_WELCOME
from gex.common.log import Log
from gex.extension import GExtension

EX_INFO = {
    "title": "Anti AFK",
    "description": "Habbo Anti AFK Mode",
    "version": __version__,
    "author": "lpmatos",
}

EX_SETTINGS = {"use_click_trigger": True, "can_leave": True, "can_delete": True}

(console, markdown, log) = (
    Console(),
    Markdown(MARKDOWN_WELCOME),
    Log("INFO", "rich", "logger").logger,
)

ext = GExtension()
