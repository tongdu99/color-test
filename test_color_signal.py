import pytest
from color_signal import ColorSignal, get_color_signal, get_color_enum

def test_get_color_signal():
    value = get_color_signal()
    assert value == 1


def test_get_color_enum():
    value = get_color_enum()
    assert value == ColorSignal.BLUE


def test_get_color_by_value():
    assert ColorSignal.BLUE == ColorSignal(3)