# -*- coding: utf-8 -*-

from time import sleep

from g_python.gextension import Extension
from g_python.hmessage import HMessage


class AutoSit:

    def __init__(self, extension: Extension):
        self.__ext = extension
        self.__loop_autosit = True

    def start(self, message: HMessage, text: str) -> None:
        if text == "!ats on":
            message.is_blocked = True
            self.__loop_autosit = True
            self.__ext.send_to_client("Auto Sit enabled!")
            self.auto()

        if text == "!ats off":
            message.is_blocked = True
            self.__loop_autosit = False
            self.__ext.info("Auto Sit disabled!")

    def auto(self) -> None:
        while self.__loop_autosit:
            self.__ext.send_to_server("{out:ChangePosture}{i:1}")
            sleep(0.2)
