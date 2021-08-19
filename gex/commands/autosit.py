# -*- coding: utf-8 -*-

from time import sleep

from g_python.gextension import Extension
from g_python.hmessage import HMessage


class AutoSit:

    def __init__(self, extension: Extension):
        """[summary]

        Args:
            extension (Extension): [description]
        """
        self.__ext = extension
        self.__loop_autosit = True

    def init(self) -> None:
        """[summary]
        """
        self.__ext.intercept_out(self.chat, "Chat", "async_modify")

    def chat(self, message: HMessage) -> None:
        """[summary]

        Args:
            message (HMessage): [description]
        """
        packet = message.packet
        text = packet.read_string().lower()
        message.is_blocked = True
        if text == "!ats on":
            self.__loop_autosit = True
            self.__ext.send_to_client(
                '{in:Whisper}{i:2}{s:"Auto Sit enabled!"}{i:0}{i:33}{i:0}{i:-1}'
            )
            self.auto_sit()

        if text == "!ats off":
            self.__loop_autosit = False
            self.__ext.send_to_client(
                '{in:Whisper}{i:2}{s:"Auto Sit disabled!"}{i:0}{i:33}{i:0}{i:-1}'
            )

    def auto_sit(self) -> None:
        """[summary]
        """
        while self.__loop_autosit:
            self.__ext.send_to_server("{out:ChangePosture}{i:1}")
            sleep(0.2)
