# -*- coding: utf-8 -*-

from time import sleep

from g_python.gextension import Extension
from g_python.hmessage import HMessage
from g_python.hpacket import HPacket

from gex.setup import date


class Awake:

    def __init__(self, extension: Extension):
        self.__ext = extension
        self.__loop_awake = True
        self.__timeout = 30

    def start(self, message: HMessage, text: str) -> None:
        if text == "!aw on":
            message.is_blocked = True
            self.__loop_awake = True
            self.__ext.info("Awake enabled!")
            self.auto()

        if text == "!aw off":
            message.is_blocked = True
            self.__loop_awake = False
            self.__ext.info("Awake disabled!")

    def auto(self) -> None:
        while self.__loop_awake:
            content = f"Datetime: {date.get_date_now()}"
            self.__ext.send_to_server(HPacket("Whisper", content, 1, 1))
            sleep(self.__timeout)
