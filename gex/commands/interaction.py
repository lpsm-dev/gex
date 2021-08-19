# -*- coding: utf-8 -*-

from time import sleep

from g_python.hmessage import HMessage
from g_python.hpacket import HPacket

from gex.commands.cmd import CMD
from gex.commands.notyping import NoTyping
from gex.commands.autosit import AutoSit
from gex.setup import date, ext, log


class Interaction(CMD):
    (loop_awake, loop_autosit, loop_autosign, blocked) = (True, True, True, False)
    timeout = 30

    def init(self) -> None:
        """[summary]"""
        log.info("Initializing awake command!")
        ext.intercept_out(self.speech_out, "Chat", "async_modify")
        no_typing, auto_sit = NoTyping(ext), AutoSit(ext)
        no_typing.init()
        auto_sit.init()

    def speech_out(self, message: HMessage) -> None:
        """[summary]

        Args:
            message (HMessage): [description]
        """
        packet = message.packet
        text = packet.read_string().lower()

        if text == "!help":
            message.is_blocked = True
            ext.send_to_client(
                '{in:Whisper}{i:2}{s:"Available commands:"}{i:0}{i:33}{i:0}{i:-1}'
            )
            ext.send_to_client(
                '{in:Whisper}{i:2}{s:"!aw on and !aw off"}{i:0}{i:33}{i:0}{i:-1}'
            )
            ext.send_to_client(
                '{in:Whisper}{i:2}{s:"!nt on and !nt off"}{i:0}{i:33}{i:0}{i:-1}'
            )
            ext.send_to_client(
                '{in:Whisper}{i:2}{s:"!ats on and !ats off"}{i:0}{i:33}{i:0}{i:-1}'
            )
            ext.send_to_client(
                '{in:Whisper}{i:2}{s:"!atsg on and !atsg off"}{i:0}{i:33}{i:0}{i:-1}'
            )

        if text == "!aw on":
            log.info("Awake enabled!")
            message.is_blocked = True
            self.loop_awake = True
            ext.send_to_client(
                '{in:Whisper}{i:2}{s:"Awake enabled!"}{i:0}{i:33}{i:0}{i:-1}'
            )
            self.awake()

        if text == "!aw off":
            log.info("Awake disabled!")
            message.is_blocked = True
            self.loop_awake = False
            ext.send_to_client(
                '{in:Whisper}{i:2}{s:"Awake disabled!"}{i:0}{i:33}{i:0}{i:-1}'
            )

        if text == "!atsg on":
            log.info("Auto Sign enabled!")
            message.is_blocked = True
            self.loop_autosign = True
            ext.send_to_client(
                '{in:Whisper}{i:2}{s:"Auto Sign enabled!"}{i:0}{i:33}{i:0}{i:-1}'
            )
            self.auto_sign()

        if text == "!atsg off":
            log.info("Auto Sign disabled!")
            message.is_blocked = True
            self.loop_autosign = False
            ext.send_to_client(
                '{in:Whisper}{i:2}{s:"Auto Sign disabled!"}{i:0}{i:33}{i:0}{i:-1}'
            )

    def awake(self) -> None:
        """[summary]"""
        while self.loop_awake:
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

    def auto_sign(self) -> None:
        """[summary]"""
        while self.loop_autosign:
            log.info("Calling Auto Sign")
            ext.send_to_server("{out:Sign}{i:1}")
            sleep(4)
