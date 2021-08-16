# -*- coding: utf-8 -*-

from os import environ
from typing import Text


class Config:
    @staticmethod
    def get_env(env: Text, default: Text = "") -> Text:
        return environ.get(env, default)
