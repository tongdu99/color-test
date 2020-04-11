
from enum import Enum


class ColorSignal(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


def get_color_signal():
    return 1

def get_color_enum():
    return ColorSignal.BLUE