from g_python.gextension import Extension
from g_python.hmessage import HMessage


class NoTyping:

    def __init__(self, extension: Extension):
        """[summary]

        Args:
            extension (Extension): [description]
        """
        self.__ext = extension
        self.__blocked = False

    def init(self) -> None:
        """[summary]
        """
        self.__ext.intercept_out(self.chat, "Chat", "async_modify")
        self.__ext.intercept_out(self.typing, "StartTyping")

    def chat(self, message: HMessage) -> None:
        """[summary]

        Args:
            message (HMessage): [description]
        """
        packet = message.packet
        text = packet.read_string().lower()
        message.is_blocked = True
        if text == "!nt on":
            self.__blocked = True
            self.__ext.send_to_client(
                '{in:Whisper}{i:2}{s:"No Typing enabled!"}{i:0}{i:33}{i:0}{i:-1}'
            )

        if text == "!nt off":
            self.__blocked = True
            self.__ext.send_to_client(
                '{in:Whisper}{i:2}{s:"No Typing disabled!"}{i:0}{i:33}{i:0}{i:-1}'
            )

    def typing(self, message: HMessage) -> None:
        """[summary]

        Args:
            message (HMessage): [description]
        """
        message.is_blocked = self.__blocked