# -*- coding: utf-8 -*-

import sys

from gex.commands.interaction import Interaction
from gex.setup import console, ext, markdown

# ================================================
# MAIN
# ================================================


def main() -> None:
    """[summary]"""
    console.print(markdown)

    try:
        ext.start()
    except ConnectionRefusedError:
        print("Please, change the G-Earth port to 9092")
        sys.exit(1)

    interaction = Interaction()
    interaction.init()


if __name__ == "__main__":
    main()
