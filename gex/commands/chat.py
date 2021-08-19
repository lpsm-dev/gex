# -*- coding: utf-8 -*-

from g_python.hmessage import HMessage

from gex.commands.autosign import AutoSign
from gex.commands.autosit import AutoSit
from gex.commands.awake import Awake
from gex.commands.cmd import CMD
from gex.commands.notyping import NoTyping
from gex.setup import ext, log


class Interaction(CMD):
    (no_typing, auto_sit, auto_sign, awake) = (
        NoTyping(ext),
        AutoSit(ext),
        AutoSign(ext),
        Awake(ext)
    )

    def init(self) -> None:
        log.info("Initializing commands!")
        ext.intercept_out(self.speech_out, "Chat", "async_modify")
        ext.intercept_out(self.no_typing.typing, "StartTyping")
        ext.intercept_in(self.block_msg, "ErrorReport", "async_modify")

    def speech_out(self, message: HMessage) -> None:
        packet = message.packet
        text = packet.read_string().lower()

        if text == "!help":
            message.is_blocked = True
            ext.info("Available commands:")
            ext.info("!aw on and !aw off")
            ext.info("!nt on and !nt off")
            ext.info("!ats on and !ats off")
            ext.info("!atsg on and !atsg off")

        self.auto_sit.start(message, text)
        self.auto_sign.start(message, text)
        self.awake.start(message, text)
        self.no_typing.start(message, text)

    @staticmethod
    def block_msg(message: HMessage):
        message.is_blocked = True
