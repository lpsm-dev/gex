# -*- coding: utf-8 -*-

from time import sleep

from g_python.hmessage import HMessage
from g_python.hpacket import HPacket

from gex.commands.cmd import CMD
from gex.setup import ext, log, date


class Interaction(CMD):
    loop = True
    blocked = False
    timeout = 30

    def init(self) -> None:
        """[summary]
        """
        log.info("Initializing awake command!")
        ext.intercept_out(self.speech_out, "Chat", "async_modify")
        ext.intercept_out(self.typing, "StartTyping")

    def speech_out(self, message: HMessage) -> None:
        """[summary]

        Args:
            message (HMessage): [description]
        """
        packet = message.packet
        text = packet.read_string()

        if text == "!aw help":
            log.info("Viewing awake helper")
            message.is_blocked = True
            ext.send_to_client('{in:Whisper}{i:2}{s:"Use the awake command to always stay awake in habbos rooms :D"}{i:0}{i:33}{i:0}{i:-1}')

        if text == "!aw on":
            log.info("Awake Enabled!")
            message.is_blocked = True
            self.loop = True
            self.awake()

        if text == "!aw off":
            log.info("Awake Disabled!")
            message.is_blocked = True
            self.loop = False

        if text == "!nt help":
            log.info("Viewing notyping helper")
            message.is_blocked = True
            ext.send_to_client('{in:Whisper}{i:2}{s:"When you star to typing, your bubble will be removed :D"}{i:0}{i:33}{i:0}{i:-1}')

        if text == "!nt on":
            log.info("Notyping Enabled!")
            message.is_blocked = True
            self.blocked = True

        if text == "!nt off":
            log.info("Notyping Disabled!")
            message.is_blocked = True
            self.blocked = False

    def awake(self) -> None:
        """[summary]
        """
        while self.loop:
            log.info("Calling awake cmd")
            content = f"Datetime: {date.get_date_now()}"
            ext.send_to_server(HPacket("Whisper", content, 1, 1))
            sleep(self.timeout)

    def typing(self, message: HMessage) -> None:
        """[summary]

        Args:
            message (HMessage): [description]
        """
        log.info("Typing handler")
        message.is_blocked = self.blocked
