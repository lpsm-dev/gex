import arrow

from gex.common.constants import DATA_FORMAT, TIMEZONE


class Date():
    def __init__(self) -> None:
        self._data_format = DATA_FORMAT

    def get_date_now(self):
        return arrow.now(TIMEZONE).format(self._data_format)
