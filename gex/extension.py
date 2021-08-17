# -*- coding: utf-8 -*-

import sys
from typing import Callable, Union

from g_python.gextension import Extension
from g_python.hdirection import Direction
from g_python.hmessage import HMessage

from gex.common.constants import EX_INFO


class GExtension(Extension):
    def __init__(self) -> None:
        super().__init__(EX_INFO, sys.argv)

        self.on_event("double_click", lambda: print("Extension has been clicked"))
        self.on_event("init", lambda: self.on_connection_init())
        self.on_event("connection_start", lambda: self.on_connection_start())
        self.on_event("connection_end", lambda: self.on_connection_end())

    @staticmethod
    def on_connection_init() -> None:
        """This method is called during the extension
        initialization with G-Earth.
        """
        print("\nInitialize G-Earth connection\n")

    def on_connection_start(self) -> None:
        """This method is called when the extension's
        connection to G-Earth happens."""
        print(
            "Connected with: {}:{}\n".format(
                self.connection_info["host"], self.connection_info["port"]
            )
        )

    @staticmethod
    def on_connection_end() -> None:
        """This method is called when the connection to
        G-Earth is lost.
        """
        print("Connection lost with G-Earth")
        print()

    def intercept_in(
        self,
        callback: Callable[[HMessage], None],
        idd: Union[int, str] = -1,
        mode: str = "default",
    ) -> None:
        """This method that intercepts incoming communications
        in Habbo.

        Args:
            callback (Callable[[HMessage], None]): [description]
            id (Union[int, str], optional): [description]. Defaults to -1.
            mode (str, optional): [description]. Defaults to "default".
        """
        self.intercept(Direction.TO_CLIENT, callback, idd, mode)

    def intercept_out(
        self,
        callback: Callable[[HMessage], None],
        idd: Union[int, str] = -1,
        mode: str = "default",
    ) -> None:
        """This method that intercepts outgoing communications
        in Habbo.

        Args:
            callback (Callable[[HMessage], None]): [description]
            id (Union[int, str], optional): [description]. Defaults to -1.
            mode (str, optional): [description]. Defaults to "default".
        """
        self.intercept(Direction.TO_SERVER, callback, idd, mode)
