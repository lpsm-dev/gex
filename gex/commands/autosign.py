# -*- coding: utf-8 -*-

from time import sleep

from g_python.gextension import Extension
from g_python.hmessage import HMessage


class AutoSign:

    def __init__(self, extension: Extension):
        self.__ext = extension
        self.__loop_autosign = True

    def start(self, message: HMessage, text: str) -> None:
        if text == "!atsg on":
            message.is_blocked = True
            self.__loop_autosign = True
            self.__ext.send_to_client(
                '{in:Whisper}{i:2}{s:"Auto Sign enabled!"}{i:0}{i:33}{i:0}{i:-1}'
            )
            self.auto()

        if text == "!atsg off":
            message.is_blocked = True
            self.__loop_autosign = False
            self.__ext.send_to_client(
                '{in:Whisper}{i:2}{s:"Auto Sign disabled!"}{i:0}{i:33}{i:0}{i:-1}'
            )

    def auto(self) -> None:
        while self.__loop_autosign:
            self.__ext.send_to_server("{out:Sign}{i:1}")
            sleep(4)
