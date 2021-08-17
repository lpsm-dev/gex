# -*- coding: utf-8 -*-

from time import sleep

from g_python.hmessage import HMessage
from g_python.hpacket import HPacket

from gex.commands.cmd import CMD
from gex.setup import date, ext, log


class Interaction(CMD):
    loop_awake, loop_autosit = True, True
    blocked = False
    timeout = 30

    def init(self) -> None:
        """[summary]"""
        log.info("Initializing awake command!")
        ext.intercept_out(self.speech_out, "Chat", "async_modify")
        ext.intercept_out(self.typing, "StartTyping")

    def speech_out(self, message: HMessage) -> None:
        """[summary]

        Args:
            message (HMessage): [description]
        """
        packet = message.packet
        text = packet.read_string().lower()

        if text == "!aw help":
            log.info("Viewing awake helper")
            message.is_blocked = True
            ext.send_to_client(
                '{in:Whisper}{i:2}{s:"Use the awake command to always stay awake in habbos rooms :D"}{i:0}{i:33}{i:0}{i:-1}'
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

        if text == "!nt help":
            log.info("Viewing notyping helper")
            message.is_blocked = True
            ext.send_to_client(
                '{in:Whisper}{i:2}{s:"When you star to typing, your bubble will be removed :D"}{i:0}{i:33}{i:0}{i:-1}'
            )

        if text == "!nt on":
            log.info("No Typing enabled!")
            message.is_blocked = True
            self.blocked = True
            ext.send_to_client(
                '{in:Whisper}{i:2}{s:"No Typing enabled!"}{i:0}{i:33}{i:0}{i:-1}'
            )

        if text == "!nt off":
            log.info("No Typing disabled!")
            message.is_blocked = True
            self.blocked = False
            ext.send_to_client(
                '{in:Whisper}{i:2}{s:"No Typing disabled!"}{i:0}{i:33}{i:0}{i:-1}'
            )

        if text == "!ats on":
            log.info("Autosit enabled!")
            message.is_blocked = True
            self.loop_autosit = True
            ext.send_to_client(
                '{in:Whisper}{i:2}{s:"Auto Sit enabled!"}{i:0}{i:33}{i:0}{i:-1}'
            )
            self.auto_sit()

        if text == "!ats off":
            log.info("Autosit disabled!")
            message.is_blocked = True
            self.loop_autosit = False
            ext.send_to_client(
                '{in:Whisper}{i:2}{s:"Auto Sit disabled!"}{i:0}{i:33}{i:0}{i:-1}'
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

    def auto_sit(self) -> None:
        """[summary]"""
        while self.loop_autosit:
            log.info("Calling auto sit")
            ext.send_to_server("{out:ChangePosture}{i:1}")
            sleep(0.1)
