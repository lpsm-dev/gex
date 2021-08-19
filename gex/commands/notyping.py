from g_python.gextension import Extension
from g_python.hmessage import HMessage


class NoTyping:

    def __init__(self, extension: Extension):
        self.__ext = extension
        self.__blocked = False

    def init(self) -> None:
        self.__ext.intercept_out(self.chat, "Chat", "async_modify")
        self.__ext.intercept_out(self.typing, "StartTyping")

    def chat(self, message: HMessage) -> None:
        packet = message.packet
        text = packet.read_string().lower()
        if text == "!nt on":
            message.is_blocked = True
            self.__blocked = True
            self.__ext.send_to_client(
                '{in:Whisper}{i:2}{s:"No Typing enabled!"}{i:0}{i:33}{i:0}{i:-1}'
            )

        if text == "!nt off":
            message.is_blocked = True
            self.__blocked = False
            self.__ext.send_to_client(
                '{in:Whisper}{i:2}{s:"No Typing disabled!"}{i:0}{i:33}{i:0}{i:-1}'
            )

    def typing(self, message: HMessage) -> None:
        """[summary]

        Args:
            message (HMessage): [description]
        """
        message.is_blocked = self.__blocked
