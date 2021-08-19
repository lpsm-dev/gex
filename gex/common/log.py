# -*- coding: utf-8 -*-

import logging
from dataclasses import dataclass
from typing import Any, Dict, NoReturn

import coloredlogs

from gex.common.constants import LOG_FORMAT, LOG_LEVELS
from gex.common.log_handlers import (BaseRichHandler, BaseStreamHandler,
                                     ContextHandler)


class SingletonLogger(type):
    _instances: Dict[Any, Any] = {}

    def __call__(cls, *args, **kwargs) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonLogger, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


@dataclass
class Log(metaclass=SingletonLogger):
    log_level: str
    log_type: str
    logger_name: str

    def __post_init__(self) -> NoReturn:
        self.log_formatter = LOG_FORMAT

        self.log_level = self.log_level if self.log_level in LOG_LEVELS else None

        self._logger = logging.getLogger(self.logger_name)
        self._logger.setLevel(self.log_level)

        if self.log_type == "rich":
            self._base_handler = BaseRichHandler()
        elif self.log_type == "stream":
            self._base_handler = BaseStreamHandler()
            self._base_configuration_log_colored()
        else:
            self._base_handler = BaseRichHandler()

        self._logger.addHandler(
            ContextHandler(self._base_handler).get_handler(
                self.log_level, self.log_formatter
            )
        )

    def _base_configuration_log_colored(self) -> coloredlogs.install:
        coloredlogs.install(
            level=self.log_level,
            logger=self.logger,
            fmt=self.log_formatter,
            milliseconds=True,
        )

    @property
    def logger(self) -> Any:
        return self._logger
