# -*- coding: utf-8 -*-

import sys
import threading
from time import sleep

from g_python.hmessage import HMessage
from g_python.hpacket import HPacket
from rich.console import Console
from rich.markdown import Markdown

from gex.constants import MARKDOWN_WELCOME
from gex.extension import GExtension
from gex.log import Log

# ================================================
# VARIABLES
# ================================================

(console, markdown, log) = (
    Console(),
    Markdown(MARKDOWN_WELCOME),
    Log("INFO", "rich", "logger").logger,
)

ext = GExtension()

# ================================================
# CLASS
# ================================================


class AFK:
    ext: GExtension
    loop = True
    timeout = 10

    def init(self) -> None:
        log.info("Initializing anti afk!")
        ext.intercept_out(callback=self.speech_out, idd="Chat")

    def speech_out(self, message: HMessage) -> None:
        packet = message.packet
        text = packet.read_string()

        if text == "!start":
            message.is_blocked = True
            self.loop = True
            antiafk = threading.Thread(target=self.anti_afk)
            antiafk.start()
            log.info("Auto AFK Enabled!")

        if text == "!stop":
            message.is_blocked = True
            self.loop = False
            log.info("Auto AFK Disabled!")

    def anti_afk(self) -> None:
        while self.loop:
            log.info("Calling anti afk...")
            ext.send_to_server(HPacket("Whisper", "hi", 1, 1))
            sleep(self.timeout)


# ================================================
# MAIN
# ================================================


def main() -> None:
    console.print(markdown)

    try:
        ext.start()
    except ConnectionRefusedError:
        print("Please, change the G-Earth port to 9092")
        sys.exit(1)

    afk = AFK()
    afk.init()


if __name__ == "__main__":
    main()
