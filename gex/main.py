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

LOOP = False

# ================================================
# FUNCTIONS
# ================================================


def anti_afk() -> None:
    global LOOP
    while LOOP:
        log.info("Calling anti afk...")
        ext.send_to_server(HPacket("Whisper", "hi", 1, 1))
        sleep(5)


# Função que intercepta pacotes de enviados pelo habbo - Saída de voz.
def speech_out(message: HMessage) -> None:
    global LOOP
    packet = message.packet
    text = packet.read_string()

    if text == "!start":
        message.is_blocked = True
        LOOP = True
        antiafk = threading.Thread(target=anti_afk)
        antiafk.start()
        log.info("Auto AFK Enabled!")

    if text == "!stop":
        message.is_blocked = True
        LOOP = False
        log.info("Auto AFK Disabled!")


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

    # Interceptação de mensagens que o meu habbo envia.
    ext.intercept_out(callback=speech_out, mode="Chat")

if __name__ == "__main__":
    main()
