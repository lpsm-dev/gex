from abc import ABCMeta, abstractmethod


class CMD(metaclass=ABCMeta):

    @abstractmethod
    def init(self) -> None:
        """Initialize the component"""
