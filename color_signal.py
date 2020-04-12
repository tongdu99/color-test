
from enum import Enum


class ColorSignal(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


def get_color_signal():
    return 1

def get_color_enum():
    return ColorSignal.BLUE

def get_color_by_value():
    colors = {"RED":1, "GREEN":2, "BLUE":3}
    return list(colors.keys())[list(colors.values()).index(3)]

def get_color_by_value2():
    colors = {"RED":1, "GREEN":2, "BLUE":3}
    color_str = {1: "RED", 2: "GREEN", 3: "BLUE"}
    return color_str[2]