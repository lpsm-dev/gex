# -*- coding: utf-8 -*-

from g_python.gextension import Extension
from g_python.hmessage import HMessage


class NoTyping:

    def __init__(self, extension: Extension):
        self.__ext = extension
        self.__blocked = False

    def start(self, message: HMessage, text: str) -> None:
        if text == "!nt on":
            message.is_blocked = True
            self.__blocked = True
            self.__ext.info("No Typing enabled!")

        if text == "!nt off":
            message.is_blocked = True
            self.__blocked = False
            self.__ext.send_to_client("No Typing disabled!")

    def typing(self, message: HMessage) -> None:
        message.is_blocked = self.__blocked
