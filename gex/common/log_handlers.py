# -*- coding: utf-8 -*-

import logging
import sys
from abc import ABCMeta, abstractmethod
from typing import Any

from pythonjsonlogger import jsonlogger
from rich.logging import RichHandler


class StrategyHandler(metaclass=ABCMeta):
    @abstractmethod
    def handler(self, log_level: str, log_formatter: str) -> Any:
        pass


class BaseRichHandler(StrategyHandler):
    @staticmethod
    def handler(log_level: str, log_formatter: str) -> RichHandler:
        rich_handler = RichHandler(rich_tracebacks=True)
        rich_handler.setLevel(log_level)
        rich_handler.setFormatter(jsonlogger.JsonFormatter(log_formatter))
        return rich_handler


class BaseStreamHandler(StrategyHandler):
    @staticmethod
    def handler(log_level: str, log_formatter: str) -> logging.StreamHandler:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(log_level)
        stream_handler.setFormatter(jsonlogger.JsonFormatter(log_formatter))
        return stream_handler


class ContextHandler:
    def __init__(self, strategy: StrategyHandler) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> StrategyHandler:
        return self._strategy

    def get_handler(self, log_level: str, log_formatter: str) -> Any:
        return self._strategy.handler(log_level, log_formatter)
