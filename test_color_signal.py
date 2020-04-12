import pytest
from lib.color_signal import ColorSignal, get_color_signal, get_color_enum, get_color_by_value, get_color_by_value2, get_multi_color_by_values

def test_get_color_signal():
    value = get_color_signal()
    assert value == 1


def test_get_color_enum():
    value = get_color_enum()
    assert value == ColorSignal.BLUE


def test_get_color_by_value_enum():
    assert ColorSignal.BLUE == ColorSignal(3)


def test_get_color_by_value_dict():
    assert "BLUE" == get_color_by_value()


def test_get_color_by_value2_dict():
    assert "GREEN" == get_color_by_value2()


def test_get_multi_color_by_values():
    expected = ["RED", "GREEN", "RED", "BLUE"]
    actual = get_multi_color_by_values()
    assert all([a == b for a, b in zip(actual, expected)])