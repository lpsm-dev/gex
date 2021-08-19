# -*- coding: utf-8 -*-

from g_python.hmessage import HMessage

from gex.commands.cmd import CMD
from gex.commands.notyping import NoTyping
from gex.commands.autosit import AutoSit
from gex.commands.autosign import AutoSign
from gex.commands.awake import Awake
from gex.setup import ext, log


class Interaction(CMD):
    loop_awake, timeout = True, 30
    (no_typing, auto_sit, auto_sign, awake) = (
        NoTyping(ext),
        AutoSit(ext),
        AutoSign(ext),
        Awake(ext)
    )

    def init(self) -> None:
        """[summary]"""
        log.info("Initializing commands!")
        ext.intercept_out(self.speech_out, "Chat", "async_modify")
        ext.intercept_out(self.no_typing.typing, "StartTyping")
        ext.intercept_in(self.block_msg, "ErrorReport", "async_modify")

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

        self.no_typing.start(message, text)
        self.auto_sit.start(message, text)
        self.auto_sign.start(message, text)
        self.awake.start(message, text)


    @staticmethod
    def block_msg(message: HMessage):
        message.is_blocked = True
