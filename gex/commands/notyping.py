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
            self.__ext.send_to_client(
                '{in:Whisper}{i:2}{s:"No Typing enabled!"}{i:0}{i:33}{i:0}{i:-1}'
            )

        if text == "!nt off":
            message.is_blocked = True
            self.__blocked = False
            self.__ext.send_to_client(
                '{in:Whisper}{i:2}{s:"No Typing disabled!"}{i:0}{i:33}{i:0}{i:-1}'
            )

    def typing(self, message: HMessage) -> None:
        message.is_blocked = self.__blocked
