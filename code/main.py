# -*- coding: utf-8 -*-

import os
import platform

def check():

    def win():
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    try:
        import g_python
    except:
        os.system("python -m pip install g_python")
        win()

check()

import sys
import threading
from time import sleep
from rich.markdown import Markdown
from rich.console import Console
from g_python import hparsers
from g_python.gextension import Extension
from g_python.hmessage import Direction, HMessage
from g_python.hpacket import HPacket

from __init__ import __version__
from src.log import Log
from src.constants import MARKDOWN_WELCOME

# ================================================
# VARIABLES
# ================================================

extension_info = {
    "title": "Anti AFK",
    "description": "Habbo Anti AFK Mode",
    "version": __version__,
    "author": "lpmatos"
}

extension_settings = {
    "use_click_trigger": True,
    "can_leave": True,
    "can_delete": True
}

loop = False

(console, markdown, log) = Console(), Markdown(MARKDOWN_WELCOME), Log("INFO", "rich", "logger").logger

# ================================================
# FUNCTIONS
# ================================================

def ANTI_AFK():
    global loop
    while loop:
        log.info("Calling anti afk...")
        ext.send_to_server(HPacket("Whisper", "hi", 1, 1))
        sleep(5)

# Função executada quando a conexão com o G-Earth está iniciando.
def on_connection_init():
    console.print(markdown)
    print()

# Função executando quando a conexão com o G-Earth starta.
def on_connection_start():
    print("Connected with: {}:{}".format(ext.connection_info["host"], 
        ext.connection_info["port"]))
    print()

# Função que intercepta pacotes quando você detalha o usuário do habbo.
def user_profile(message: HMessage):
    profile = hparsers.HUserProfile(message.packet)
    log.info(profile)

# Função que intercepta pacotes quando você anda no habbo.
def on_walk(message: HMessage):
    (x, y) = message.packet.read("ii")
    print("\n==========================================")
    print("= Walking to x:{}, y={}".format(x, y))
    print("==========================================")
    ext.send_to_server(HPacket("AvatarExpression", 1))

# Função que intercepta pacotes de enviados pelo habbo - Saída de voz. 
def speech_out(message: HMessage):
    global loop
    packet = message.packet
    text = packet.read_string()

    if text == "!start":
        message.is_blocked = True
        loop = True
        ANTIAFK = threading.Thread(target=ANTI_AFK)
        ANTIAFK.start()
        ext.send_to_client("{in:Whisper}{i:2}{s:'Auto AFK Enabled!'}{i:0}{i:33}{i:0}{i:-1}")

    if text == "!stop":
        message.is_blocked = True
        loop = False
        ext.send_to_client("{in:Whisper}{i:2}{s:'Auto Disabled!'}{i:0}{i:33}{i:0}{i:-1}")

# Função que intercepta pacotes de enviados pelos outros habbos - Entrada de voz. 
def speech_in(message: HMessage):
    index, text, _, bubble, _, id = message.packet.read("isiiii")
    print("\n==========================================")
    print(f"= Message receive -> index : {index}, message : {text}, bubble : {bubble}")
    print("==========================================")

# ================================================
# MAIN
# ================================================

if __name__ == "__main__":
    ext = Extension(extension_info, sys.argv, extension_settings)

    ext.on_event("double_click", lambda: print("Extension has been clicked"))
    ext.on_event("init", on_connection_init)
    ext.on_event("connection_start", on_connection_start)
    ext.on_event("connection_end", lambda: print("Connection ended"))

    try:
        ext.start()
    except ConnectionRefusedError:
        print("Please, change the G-Earth port to 9092")
        sys.exit(1)

    # Interceptação de dados quando o usuário anda no habbo.
    ext.intercept(Direction.TO_SERVER, on_walk, "MoveAvatar")

    # Intercaptação de ações de extender o profile do usuário.
    ext.intercept(Direction.TO_CLIENT, user_profile, "ExtendedProfile")

    # Interceptação de mensagens que o meu habbo envia.
    ext.intercept(Direction.TO_SERVER, speech_out, "Chat")

    # Interceptação de mensagens que os outros habbos enviam.
    # ext.intercept(Direction.TO_CLIENT, speech_in, "Chat")
