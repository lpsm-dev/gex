# -*- coding: utf-8 -*-

from time import sleep

from g_python.hmessage import HMessage
from g_python.hpacket import HPacket

from gex.setup import ext, log
from gex.commands.cmd import CMD


class AwakeCMD(CMD):
    loop = True
    timeout = 10

    def init(self) -> None:
        """[summary]
        """
        log.info("Initializing awake command!")
        ext.intercept_out(callback=self.speech_out, idd="Chat", mode="async_modify")

    def speech_out(self, message: HMessage) -> None:
        """[summary]

        Args:
            message (HMessage): [description]
        """
        packet = message.packet
        text = packet.read_string()

        if text == "!awake on":
            log.info("Awake Enabled!")
            message.is_blocked = True
            self.loop = True
            self.anti_afk()

        if text == "!awake off":
            log.info("Awake Disabled!")
            message.is_blocked = True
            self.loop = False

    def anti_afk(self) -> None:
        """[summary]
        """
        while self.loop:
            log.info("calling awake cmd...")
            ext.send_to_server(HPacket("Whisper", "hi", 1, 1))
            sleep(self.timeout)
